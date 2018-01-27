import time
import asyncio
import functools


class Shutdown(Exception):
    pass


class ServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.write('Welcome.')

    def data_received(self, data):
        if not data:
            return
        message = data.decode('ascii')
        command = message.strip().split(' ')[0].lower()
        args = message.strip().split(' ')[1:]
        if not hasattr(self, 'command_%s' % command):
            self.write('Invalid command: %s' % command)
            return

        try:
            return getattr(self, 'command_%s' % command)(*args)
        except Exception as ex:
            self.write('Error: %s\n' % str(ex))

    def write(self, msg_string):
        msg_string += '\n'
        self.transport.write(msg_string.encode('ascii', 'ignore'))

    def command_add(self, *args):
        args = [int(i) for i in args]
        self.write('%d' % sum(args))

    def command_shutdown(self):
        self.write('Okay. Shutting down.')
        raise KeyboardInterrupt


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ServerProtocol, '127.0.0.1', 8000)
    asyncio.ensure_future(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("exit")

"""
yum -y install telnet
[root@mhc file_test]# telnet 127.0.0.1 8000
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
Welcome.
add 3 5
8
sddsfdf
Invalid command: sddsfdf
shutdown
Okay. Shutting down.
Connection closed by foreign host.
"""