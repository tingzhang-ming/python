

def t1():
    for i in range(10):
        print i
        i = i+1


def t2():
    a = {
        "a": 1,
        "b": 2,
    }
    print a
    a.pop("a")
    print a
# {'a': 1, 'b': 2}
# {'b': 2}


def t3():
    for i in range(0):
        print i


def get_half_index(target):
    length = len(target)
    if length == 1:
        return 1
    return length / 2


def t4():
    print get_half_index([1])
    print get_half_index([1,2])
    print get_half_index([1,2,3])
    print get_half_index([1, 2, 3, 4])


def t5():
    a = 'Exception in thread Thread-8:\nTraceback (most recent call last):\n  File "/usr/local/lib/python2.7/threading.py", line 808, in __bootstrap_inner\n    self.run()\n  File "/usr/local/lib/python2.7/threading.py", line 761, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/engine/flow.py", line 545, in _call_sub_task\n    res = self._call_task_fn(args)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/engine/flow.py", line 569, in _call_task_fn\n    return self.task_fn(**args_map)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/tasks/server.py", line 107, in create\n    inject_files["/etc/my.cnf"] = collect_proxy_my_cnf(context, group_id)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/tasks/proxy.py", line 100, in collect_proxy_my_cnf\n    port = DBInstanceGroup.get_extend_value(context, group_id)["mysql_port"]\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/db/data_models/group.py", line 33, in get_extend_value\n    db_info = cls.find_by(id=group_id)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/db/models.py", line 103, in find_by\n    raise exception.ModelNotFoundError("{} Not Found with conditions:{}".format(cls.__name__, conditions))\nModelNotFoundError: DBInstanceGroup Not Found with conditions:{\'id\': <trove.common.context.TroveContext object at 0x4d1f8d0>}\n\nException in thread Thread-9:\nTraceback (most recent call last):\n  File "/usr/local/lib/python2.7/threading.py", line 808, in __bootstrap_inner\n    self.run()\n  File "/usr/local/lib/python2.7/threading.py", line 761, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/engine/flow.py", line 545, in _call_sub_task\n    res = self._call_task_fn(args)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/engine/flow.py", line 569, in _call_task_fn\n    return self.task_fn(**args_map)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/tasks/server.py", line 107, in create\n    inject_files["/etc/my.cnf"] = collect_proxy_my_cnf(context, group_id)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/tasks/proxy.py", line 100, in collect_proxy_my_cnf\n    port = DBInstanceGroup.get_extend_value(context, group_id)["mysql_port"]\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/db/data_models/group.py", line 33, in get_extend_value\n    db_info = cls.find_by(id=group_id)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/db/models.py", line 103, in find_by\n    raise exception.ModelNotFoundError("{} Not Found with conditions:{}".format(cls.__name__, conditions))\nModelNotFoundError: DBInstanceGroup Not Found with conditions:{\'id\': <trove.common.context.TroveContext object at 0x4d1f8d0>}\n\nException in thread Thread-6:\nTraceback (most recent call last):\n  File "/usr/local/lib/python2.7/threading.py", line 808, in __bootstrap_inner\n    self.run()\n  File "/usr/local/lib/python2.7/threading.py", line 761, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/engine/flow.py", line 393, in run\n    self._run(flow_id, args)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/engine/flow.py", line 428, in _run\n    res = self._call_sub_tasks(db_info.id, call_args)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/engine/flow.py", line 514, in _call_sub_tasks\n    raise FlowError("sub task:{} failed, msg:{}".format(sub_task.id, sub_task.result))\nFlowError: sub task:f4d40fd6-f15d-419c-8731-f5a019b48ce5 failed, msg:DBInstanceGroup Not Found with conditions:{\'id\': <trove.common.context.TroveContext object at 0x4d1f8d0>}\n\n'
    print a


if __name__ == '__main__':
    t5()
