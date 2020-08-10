#!/usr/bin/env python3
# author: DYzZs

import requests
import os, sys
from fake_useragent import UserAgent



# 判断返回状态码
def switch(http_code):
    switcher = {
        200: '正常访问',
        301: '永久转移,重定向',
        302: '暂时转移,重定向',
        401: '未经授权',
        403: '禁止访问',
        404: '页面不见',
        500: '服务端error',
        503: '暂停服务',
    }
    return switcher.get(http_code, 'other status code!')


def getUrl(file_name):
    # 随机伪造User-Agent头
    ua = UserAgent(verify_ssl=False, use_cache_server=False).random
    headers = {
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }
    # 获取文件路径
    file_path = os.path.join(os.getcwd(), file_name)
    if not os.path.exists(file_path):
        print(file_name+'not exit!')
    else:
        # 读取域名
        with open(file_path) as f:
            for domain in f.readlines():
                domain = domain.strip("\n")
                pro = ['http://', 'https://']
                for p in pro:
                    url = f'{p}{domain}'
                    try:
                        requests.packages.urllib3.disable_warnings()
                        resp = requests.get(url=url, headers=headers, timeout=5, verify=False)
                        http_code = resp.status_code
                        result = switch(http_code)
                        print(result+":"+url)
                    except Exception as e:
                        print("gg:"+url)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        getUrl(filename)
