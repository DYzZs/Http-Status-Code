#!/usr/bin/env python3
#author: D1sAbl4

import requests
import os, sys, time
import threading
from fake_useragent import UserAgent



# 判断返回状态码
def switch(http_code):
    switcher = {
        200: '正常访问',
        301: '永久转移,重定向',
        302: '暂时转移,重定向',
        303: '303',
        307: '307',
        401: '未经授权',
        403: '禁止访问',
        404: '页面不见',
        405: '请求方法错误',
        500: '服务端error',
        503: '暂停服务',
    }
    return switcher.get(http_code, 'other status code!')


def getUrl(domain, sem):

    # 随机伪造User-Agent头
    ua = UserAgent(verify_ssl=False, use_cache_server=False).random
    headers = {
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }

    #请求http, https
    pro = ['http://', 'https://']

    for p in pro:
        sem.acquire()  
        url = f'{p}{domain}'
        try:
            requests.packages.urllib3.disable_warnings()
            resp = requests.get(url=url, headers=headers, timeout=5, verify=False)
            http_code = resp.status_code
            result = switch(http_code)
            print(result+":"+url)
        except Exception as e:
            print("gg:"+url)
        sem.release()  


if __name__ == '__main__':
    time1 = time.time()
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        sem = threading.BoundedSemaphore(5)
        # 获取文件路径
        file_path = os.path.join(os.getcwd(), filename)
        Threads = []
        if not os.path.exists(file_path):
            print(filename + 'not exit!')
        else:
            with open(file_path) as f:   # 读取域名
                for domain in f.readlines():
                    domain = domain.rstrip("\n")
                    t = threading.Thread(target=getUrl, args=(domain, sem))
                    t.start()
                    Threads.append(t)

                for n in Threads:
                    n.join()
                print("uage time:%f " %(time.time() - time1))