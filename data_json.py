#coding:utf-8

#http://seputu.com  上的盗墓笔记标题、章节及链接

import re
import json
import requests
from lxml import etree

data = []
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
url = 'http://seputu.com'
response = requests.get(url,headers = headers)

pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
selector = etree.HTML(response.text)
content = selector.xpath('.//div[@class="mulu"]')
for mulu in content:
    h2 = mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(h2)>0:
        title = h2[0]
        a = mulu.xpath('./div[@class="box"]/ul/li/a')
        for i in a:
            href = i.xpath('./@href')
            data_chapter = i.xpath('./@title')[0]
            match = pattern.search(data_chapter)
            if match!=None:
                date = match.group(1)
                chapter = match.group(2)
                data.append({'title':title,'chapter':chapter,'href':href,'date':date})
                print(data)
with open('daomubiji.json','w') as fp:
    json.dump(data,fp=fp,indent=4)