#!/usr/bin/env python
# -*- coding:utf-8 -*-

#   Author  :
#   E-mail  :
#   Date    :
#   Desc    :   下载图片脚本

import requests

PATH = '/Users/chenqianping/Desktop/170409'   #保存图片的路径

# 图片的url
URLS = [
'[pic1]: http://upload-images.jianshu.io/upload_images/1845730-3f900b185cc6d271.jpg "曹操"',
'[pic2]: http://upload-images.jianshu.io/upload_images/1845730-61074190b26336fa.jpg "蔡文姬"',
]


class Img(object):
    def __init__(self, url):
        self.file_name = url.split('/')[-1]
        self.url = url
        self.path = PATH+'/'+self.file_name

    @property
    def data(self):
        r = requests.get(self.url)
        return r.content

    def save(self):
        with open(self.path, 'wb') as fb:
            fb.write(self.data)

for i, url in enumerate(URLS):
    url = url.split(' ')[1]
    Img(url).save()
    print u'第{}／共{}：{}'.format(i+1, len(URLS), 'sucess')