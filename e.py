

def t1():
    a = [2, 3, 1]
    i = 0
    print a[:i+1]
    tmp = a[i+1:]
    tmp.reverse()
    print tmp
    print a
    print a[:i+1].extend(tmp)


def t2():
    print range(0, 9, 3)


# innodb_buffer_pool_size = 640M
# tmp_table_size = 64M
# max_heap_table_size = 64M
# query_cache_size = 10M
# query_cache_limit = 1M
# table_definition_cache = 400
# innodb_additional_mem_pool_size = 100M
# innodb_log_file_size = 128M
# innodb_log_buffer_size = 8M
# innodb_flush_log_at_trx_commit = 1
# innodb_lock_wait_timeout = 30
import json
def t3():
    print json.dumps({'plugin-load': 'semisync_master.so;semisync_slave.so',
                      'skip-name-resolve': 0,
                      'tmp_table_size': '64M',
                      'max_heap_table_size': '64M',
                      'query_cache_size': '1M',
                      'table_definition_cache': 400,
                      'innodb_additional_mem_pool_size': '100M',
                      'innodb_log_file_size': '128M',
                      'innodb_log_buffer_size': '8M',
                      'innodb_flush_log_at_trx_commit': 1,
                      'innodb_lock_wait_timeout': 30

                      })


import time
def t4():
    print time.time()

if __name__ == '__main__':
    t4()

