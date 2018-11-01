#!/usr/bin/env python
# encoding: utf-8 
"""
@version: v1.0
@ethanerwu 
@time: 2018/5/18 15:27
"""

import requests,os,sys


def  urlresout(url):
      urlhttp= os.popen('curl -m 10  -L -o /dev/null -skw "http_code: %{http_code}"  "'+url+'" ').read()
      return  urlhttp


if __name__ == '__main__':
      ip=sys.argv[1]
      url=sys.argv[2].split('//')[-1]
     # url2=url.split('//')[-1]
      uurl="http://"+ip+"/"+url
   #http://1.1.1.1/33872.liveplay.myqcloud.com/live/33872_enson_test.flv
      print urlresout(uurl).split(':')[-1]