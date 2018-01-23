# encoding: utf-8
import re

text = """
<a class="p_n_p_prefix" href="http://www.cnblogs.com/codefish/p/5924481.html">« </a>
上一篇：
<a href="http://www.cnblogs.com/codefish/p/5924481.html" title="发布于2016-09-30 18:00">[Nancy On .Net Core Docker] 轻量级的web框架</a>
<br>
"""


print re.findall('(?<=(?:<a href=")).*(?=(?:" title))', text)
