#coding=utf8
import requests
import json
import time
from lxml import etree
from w_post.models import JianShuPost
from datetime import datetime
headers = {
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With" : "XMLHttpRequest",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
'Referer': 'http://www.jianshu.com/search?utf8=%E2%9C%93&q=python',
            "Accept-Language":"pzh-CN,zh;q=0.8",

        }
def load_list(kw,page):
    url = "http://www.jianshu.com//search/do"
    params ={"q":kw,
              'page':page,
              'order_by':"default",}
    response = requests.get(url,params=params,headers=headers).text
    dict = json.loads(response)
    return dict.get('entries')
def load_detail(slug):
    url='http://www.jianshu.com/p/%s'%slug
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    }
    response = requests.get(url,headers=headers).text
    selector = etree.HTML(response)

    ele =selector.xpath('//div[@class="show-content"]')[0]
    content = etree.tostring(ele,encoding='gbk').decode('gbk').replace(r"<?xml version='1.0' encoding='gbk'?>",'')
    return content

def manage(start,end,kw):
    for i in range(start,end+1):
        print('正在爬取内容')
        d = load_list(kw,i)
        for post in d:
            time.sleep(0.4)
            p = JianShuPost()
            p.title=post['title']
            p.slug=post['slug']
            p.content=''
            p.datetime=datetime.strptime(post['first_shared_at'], '%Y-%m-%dT%H:%M:%S.000Z')
            p.author=post['user']['nickname']
            p.author_id=int(post['user']['id'])
            p.intro = post['content']
            p.keyword = kw

            content = load_detail(p.slug)
            p.content =content
            p.save()
        print('end******************')






if __name__ == '__main__':
    d=load_list('python',1)
    file = open('jinshu.html','a')
    for i in d:
        slug = i.get('slug')
        content = load_detail(slug)
        print(content)
        file.write(content.decode('gbk'))
    file.close()
    print('end')
