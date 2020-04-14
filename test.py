#! weibo/Scripts/python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/03/23 17:01:03
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib

import requests
from bs4 import BeautifulSoup
import json
'''
测试代码
'''
def request(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Cookie': 'MLOGIN=1;WEIBOCN_FROM=;SCF=Art5xhYEloxGpUp_gy0CrNMb39zsZpmvPKFDk3O7TwWj-9gseA5BGJay3NJHhBR0ajxurXNIaTSpkxwX6HWOP9E.;_T_WM=26723672006;SSOLoginState=1583609025;M_WEIBOCN_PARAMS=uicode%3D20000174;XSRF-TOKEN=a88288;SUHB=08JrogEnY36tjx;SUB=_2A25zZ4SRDeRhGeBG7FUV9ifPzT2IHXVQqyzZrDV6PUJbkdAKLWjhkW1NQeFDpIhkzgWQekAYw2p2d7DA9x9ywS4B'
    }
    results = requests.get(url,headers = headers)
    return BeautifulSoup(results.text)
    

def Info():
    soup = request("https://m.weibo.cn/api/container/getIndex?is_hot[]=1&is_hot[]=1&jumpfrom=weibocom&type=uid&value=5034066423&containerid=1005055034066423")
    results_json = json.loads(str(soup))
    print(results_json['data']['userInfo']['follow_count'],results_json['data']['userInfo']['followers_count'])

Info()