<pre><code>
过滤器名称	    说明    
safe	        渲染时值不转义
capitialize	把值的首字母转换成大写，其他子母转换为小写
 lower	        把值转换成小写形式 
 upper	        把值转换成大写形式 
 title	        把值中每个单词的首字母都转换成大写
 trim	        把值的首尾空格去掉
 striptags	渲染之前把值中所有的HTML标签都删掉
 join 	        拼接多个值为字符串
 replace	替换字符串的值
 round	        默认对数字进行四舍五入，也可以用参数进行控制
 int 	        把值转换成整型
 
 在for循环中，jinja2还提供了一些特殊的变量，用以来获取当前的遍历状态：

变量	描述
loop.index	当前迭代的索引（从1开始）
loop.index0	当前迭代的索引（从0开始）
loop.first	是否是第一次迭代，返回bool
loop.last	是否是最后一次迭代，返回bool
loop.length	序列中的项目数量
loop.revindex	到循环结束的次数（从1开始）
loop.revindex0	到循环结束的次数(从0开始）
</code></pre>