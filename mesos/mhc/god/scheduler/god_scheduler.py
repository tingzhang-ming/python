import os
import sys
import socket
from twitter.common import app, log
from twitter.common.log.options import LogOptions
from twitter.common.exceptions import ExceptionalThread
from twitter.common.http import HttpServer
from god.common import pkgutil
from zk_state import ZooKeeperStateProvider, StateProvider, Scheduler
from kazoo.client import KazooClient
from god.common import zookeeper
from god.scheduler.password import PasswordBox
from god.common.utils import *
from addict import Dict
from god.scheduler.scheduler import GodScheduler
from pymesos import MesosSchedulerDriver
from http import GodServer
from god.common import kazoo_log
from twitter.common.quantity.parse_simple import InvalidTime, parse_time, parse_data, InvalidData
from twitter.common.quantity import Amount, Data, Time

FRAMEWORK_NAME = 'god'
HYALINE_MODULE = 'god.scheduler'
ASSET_RELPATH = 'assets'
ZK_URL = 'zk://127.0.0.1:2181/god8'
SCHEDULER_KEY = '73SZAptK4K6i2sB8fw6B0aQf0qLO6zmw'
FRAMEWORK_USER = 'root'
PORT = 55001
FW_PRINCIPLE = 'mhc'
FW_ROLE = 'mhc'
EXECUTOR_CMD = 'god_executor'
MASTER = '127.0.0.1:5050'
FAILOVER_TIMEOUT = "15d"

LogOptions.disable_disk_logging()
LogOptions.set_stderr_log_level('google:DEBUG')

def proxy_main():
    # app.add_option(
    #     '--cnf',
    #     dest='cnf',
    #     default=None,
    #     help='mhc.cnf')

    def main(args, options):
        log.info("God scheduler run...")
        work_dir = "/tmp/mhc_framework"
        web_assets_dir = os.path.join(work_dir, "web")
        pkgutil.unpack_assets(web_assets_dir, HYALINE_MODULE, ASSET_RELPATH)
        logger = kazoo_log.Logger()
        logger.set_log_dir("/tmp/zookeeper.log")
        try:
            _, zk_servers, zk_root = zookeeper.parse(ZK_URL)
            kazoo = KazooClient(hosts=zk_servers, logger=logger)
            kazoo.start()
        except:
            print "Can't connect to zookeeper."
            sys.exit(1)
        password_box = PasswordBox(SCHEDULER_KEY)
        log.info("Using ZooKeeper (path: %s) for state storage." % zk_root)
        state_provider = ZooKeeperStateProvider(kazoo, zk_root, password_box)

        try:
            old_state = state_provider.load_scheduler_state()
        except StateProvider.Error as e:
            app.error(e.message)
            old_state = None
        framework_failover_timeout = parse_time(FAILOVER_TIMEOUT)
        framework_info = Dict()
        framework_info.user = FRAMEWORK_USER
        framework_info.name = FRAMEWORK_NAME
        framework_info.checkpoint = True
        framework_info.failover_timeout = framework_failover_timeout.as_(Time.SECONDS),
        framework_info.hostname = socket.gethostname()
        framework_info.role = FW_ROLE
        framework_info.webui_url = "http://{}:{}".format(framework_info.hostname, PORT)
        framework_info.principal = FW_PRINCIPLE
        if old_state:
            state = Scheduler()
            restructure(old_state, state)
            log.info("Successfully restored scheduler state.")
            if state.framework_id:
                framework_info.id.value = state.framework_id
        else:
            log.info("No scheduler state to restore.")
            state = Scheduler()
        state_provider.dump_scheduler_state(state)
        scheduler = GodScheduler(
            state,
            state_provider,
            framework_info,
            EXECUTOR_CMD,
            kazoo,
            SCHEDULER_KEY)

        scheduler_driver = MesosSchedulerDriver(
            scheduler,
            framework_info,
            MASTER,
            use_addict=True,
        )

        scheduler_driver.start()
        server = HttpServer()
        my_server = GodServer(scheduler, web_assets_dir)
        server.mount_routes(my_server)
        et = ExceptionalThread(
            target=server.run, name="httpserver", args=('0.0.0.0', PORT, 'cherrypy'))
        et.daemon = True
        et.start()
        # initialize API

        try:
            # Wait for the scheduler to stop.
            # The use of 'stopped' event instead of scheduler_driver.join() is necessary to stop the
            # process with SIGINT.
            while not scheduler.stopped.wait(timeout=0.5):
                time.sleep(1)
        except KeyboardInterrupt:
            log.info('Interrupted, exiting.')
        else:
            log.info('Scheduler exited.')
        finally:
            kazoo.stop()

        app.shutdown(1)

    app.main()

if __name__ == '__main__':
    proxy_main()
