a='Exception in thread Thread-1:\nTraceback (most recent call last):\n  File "/usr/local/lib/python2.7/threading.py", line 808, in __bootstrap_inner\n    self.run()\n  File "/usr/local/lib/python2.7/threading.py", line 761, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/engine/flow.py", line 393, in run\n    self._run(flow_id, args)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/engine/flow.py", line 430, in _run\n    res = self._call_task_fn(call_args)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/engine/flow.py", line 569, in _call_task_fn\n    return self.task_fn(**args_map)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/trove/taskmanager/tasks/server.py", line 229, in create\n    scheduler_hints=scheduler_hints)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/python_novaclient-0.1.0-py2.7.egg/novaclient/v1_1/servers.py", line 615, in create\n    **boot_kwargs)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/python_novaclient-0.1.0-py2.7.egg/novaclient/v1_1/base.py", line 163, in _boot\n    return_raw=return_raw, **kwargs)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/python_novaclient-0.1.0-py2.7.egg/novaclient/base.py", line 145, in _create\n    _resp, body = self.api.client.post(url, body=body)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/python_novaclient-0.1.0-py2.7.egg/novaclient/client.py", line 246, in post\n    return self._cs_request(url, \'POST\', **kwargs)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/python_novaclient-0.1.0-py2.7.egg/novaclient/client.py", line 216, in _cs_request\n    **kwargs)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/python_novaclient-0.1.0-py2.7.egg/novaclient/client.py", line 197, in _time_request\n    resp, body = self.request(url, method, **kwargs)\n  File "/home/mahongchao/env_ktrove/lib/python2.7/site-packages/python_novaclient-0.1.0-py2.7.egg/novaclient/client.py", line 191, in request\n    raise exceptions.from_response(resp, body, url, method)\nBadRequest: Invalid imageRef provided. (HTTP 400)\n\n'
print a

