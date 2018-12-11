# encoding: utf-8
import requests
import backoff
import time

# 可组合使用，即加多个@backoff


def lookup_max_time():
    return 11


def fatal_code(e):
    return 400 <= e.response.status_code < 500


# @backoff.on_exception(backoff.expo, requests.exceptions.RequestException)
# @backoff.on_exception(backoff.expo,
#                       (requests.exceptions.RequestException,
#                        requests.exceptions.Timeout))
# @backoff.on_exception(backoff.expo,
#                       requests.exceptions.RequestException,
#                       max_time=60)
# @backoff.on_exception(backoff.expo,
#                       requests.exceptions.RequestException,
#                       max_time=lookup_max_time)
# @backoff.on_exception(backoff.expo,
#                       requests.exceptions.RequestException,
#                       max_tries=5)
@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_time=300,
                      giveup=fatal_code)
def get_url(url):
    print(url)
    print(time.time())
    return requests.get(url)


# 当返回空列表时，按斐波那契序列退避重试，max_value 是fibo的初始化参数
# @backoff.on_predicate(backoff.fibo, lambda x: x == [], max_value=13)
# 每隔一秒尝试
@backoff.on_predicate(backoff.constant, interval=1)
def poll_for_messages(queue):
    return queue.get()


"""
事件处理

两个backoff装饰器都可以选择使用关键字参数on_success、on_backoff和on_giveup接受事件处理程序函数。
这在报告统计或执行其他自定义日志方面可能有用。
处理程序必须是一个接受一个字典参数的一元签名的可调用文件。此字典包含调用的详细信息。有效键包括：

target：引用调用的函数或方法

args：func的位置参数

kwargs ： func的关键字参数

tries： 到目前为止的调用次数

elapsed： 到现在为止经过的时间

wait： 等待秒（仅on_backoff处理）

value： 触发退避值（仅用on_predicate装饰器）
"""


def backoff_hdlr(details):
    print(details)

# @backoff.on_exception(backoff.expo,
#                       requests.exceptions.RequestException,
#                       on_backoff=backoff_hdlr)
# @backoff.on_exception(backoff.expo,
#                       requests.exceptions.RequestException,
#                       on_backoff=[backoff_hdlr, backoff_hdlr2])


"""
要在基于asyncio的异步代码中使用backoff，您只需要将backoff.on_exception或backoff.on_predicate应用于协同例程。
您还可以使用接口是相同的on_success、on_backoff和on_giveup事件处理程序的协同程序。
下面的示例使用aiohttp 异步HTTP Client/Server库。
"""

# @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_time=60)
# async def get_url2(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()


# 如果使用Python 3.4，可以使用@asyncio.coroutine和yield from：
# @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_time=60)
# @asyncio.coroutine
# def get_url_py34(url):
#     with aiohttp.ClientSession() as session:
#         response = yield from session.get(url)
#         try:
#             return (yield from response.text())
#         except Exception:
#             response.close()
#             raise
#         finally:
#             yield from response.release()


# 日志配置
# import logging
# logging.getLogger('backoff').addHandler(logging.StreamHandler())
# logging.getLogger('backoff').setLevel(logging.ERROR)

if __name__ == '__main__':
    get_url("http://sdfsadf")
