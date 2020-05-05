# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 17:33
# @Author  : shajiu
# @FileName: hello_get.py
# @Software: PyCharm
# CGI处理模块
import cgi, cgitb
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()
# 获取数据
site_name = form.getvalue('name')
site_url  = form.getvalue('url')
print ("Content-type:text/html")
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>菜鸟教程 CGI 测试实例</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s官网：%s</h2>" % (site_name, site_url))
print ("</body>")
print ("</html>")