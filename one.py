#coding:utf-8
import re

list = ['[2012-5-19 3:3:52] 七星鲁王 第一章 血尸']
pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
str = list[0]
match = pattern.search(str)
print(match.group(2))


str_we = 'we work welcome '
we_pattern = re.compile(r'we')
we = re.match(we_pattern,str_we)
print(we.group())