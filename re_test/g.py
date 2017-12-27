import re


datas = [
    'dbelt',
    'gct-client-logs',
    'dbcm/',
    'dbcm/v0.1.0/',
    'dbcm/v0.1.0/DBelt_DBCM_MySQL_Demontration.mp4',
    'dbcm/v0.1.0/DBelt_DBCM_Redis_Demontration.mp4',
    'dbcm/v0.2.0/',
    'dbcm/v0.2.0/DBelt_DBCM_MySQL_Demo.mp4',
    'dbcm/v0.2.0/DBelt_DBCM_Redis_Demo.mp4',
    'mhc/test.txt',
    'mhc/test2.txt',
    'test.jpg',
    'test/backups/mysqlms256-mysql-backup-2017-12-26T07-58-33Z/mysqlms256-mysql-backup-2017-12-26T07-58-33Z_00000001',
    'test/backups/mysqlms256-mysql-backup-2017-12-26T07-58-33Z/mysqlms256-mysql-backup-2017-12-26T07-58-33Z_00000002',
    'test/configs/mysqlms256-mysql-config-2017-12-26T07-53-37Z',
    'test/configs/mysqlms256-mysql-config-2017-12-26T07-55-02Z',
    'test/configs/test_my.cnf',
]


def t1():
    d = 'test/backups/'
    patt = '(^%s)/.*[^/]' % d.rstrip('/')
    for data in datas:
        res = re.search(patt, data)
        if res:
            print res.group()


if __name__ == '__main__':
    t1()
