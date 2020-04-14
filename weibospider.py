#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   iphonequeste.py
@Time    :   2020/04/10 16:01:11
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
import json
import re
import data_save_to_csv as ds

headers = {#request header
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Cookie': 'MLOGIN=1;WEIBOCN_FROM=;SCF=Art5xhYEloxGpUp_gy0CrNMb39zsZpmvPKFDk3O7TwWj-9gseA5BGJay3NJHhBR0ajxurXNIaTSpkxwX6HWOP9E.;_T_WM=26723672006;SSOLoginState=1583609025;M_WEIBOCN_PARAMS=uicode%3D20000174;XSRF-TOKEN=a88288;SUHB=08JrogEnY36tjx;SUB=_2A25zZ4SRDeRhGeBG7FUV9ifPzT2IHXVQqyzZrDV6PUJbkdAKLWjhkW1NQeFDpIhkzgWQekAYw2p2d7DA9x9ywS4B'
    }

def iphone_requests(i_d,n):#Request by phone
    try:
        results = requests.get('https://m.weibo.cn/api/container/getIndex?containerid=230413{}_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=230283{}&page_type=03&page={}'.format(i_d,i_d,n),headers = headers)
        results.encoding = results.apparent_encoding#获取网页编码，对网页内容进行编码，防止乱码产生
        results_json = json.loads(results.text)
        # print('https://m.weibo.cn/api/container/getIndex?containerid=230413{}_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=230283{}&page_type=03&page={}'.format(i_d,i_d,n))
        return results_json
    except :
        print('https://m.weibo.cn/api/container/getIndex?containerid=230413{}_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=230283{}&page_type=03&page={}'.format(i_d,i_d,n))
        return iphone_requests(id,n+1)

def request_info(url):#request information
    results = requests.get(url,headers = headers)
    return BeautifulSoup(results.text,features="html.parser")

def Info(i_d):#return personal information:nickname/introduction/time/credit
    soup = request_info("https://m.weibo.cn/api/container/getIndex?containerid=230283{}_-_INFO&title=%E5%9F%BA%E6%9C%AC%E8%B5%84%E6%96%99&luicode=10000011&lfid=230283{}".format(i_d,i_d))
    results_json = json.loads(str(soup))
    information = []
    for i in results_json['data']['cards'][0]['card_group']:
        try:
            information.append({i['item_name']:i['item_content']})
        except:
            pass
    return information
        
def follow(i_d):#The number of people returning to follow and how many people follow:follow count/followers count
    soup = request_info("https://m.weibo.cn/api/container/getIndex?is_hot[]=1&is_hot[]=1&jumpfrom=weibocom&type=uid&value={}&containerid=100505{}".format(i_d,i_d))
    results_json = json.loads(str(soup))
    FollowList = []
    FollowList.append({"关注:":results_json['data']['userInfo']['follow_count']})
    FollowList.append({"被关注:":results_json['data']['userInfo']['followers_count']})
    return FollowList


def main_info(i_d,n):#return weibo's information:love/comment/forward/time/main information
    for count in range(1,n):
        soup = iphone_requests(i_d,count)
        for i in soup['data']['cards']:

            try:
                # print("点赞:",i["mblog"]['attitudes_count'],"评论:",i["mblog"]['comments_count'],"转发:",i["mblog"]['reposts_count'],"时间:",i["mblog"]["created_at"])
                ds.save_main_information({'love':i["mblog"]['attitudes_count'],
                                        'comment':i["mblog"]['comments_count'],
                                        'forward':i["mblog"]['reposts_count'],
                                        'time':i["mblog"]["created_at"],
                                        'main_information':i["mblog"]['text'].split('<')[0]})
                # print("主要信息:",i["mblog"]['text'].split('<')[0],end='\n\n')
            except:
                pass

def personal_info(i_d):
    ifomation = Info(i_d)
    fan = follow(i_d)
    name = {}
    for i in ifomation+fan:
        name.update(i)
    ds.save_personal_information(name)

def Main(i_d,n):
    personal_info(i_d)
    main_info(i_d,n)

if __name__ == "__main__":
    i_d = input("请输入id:")
    n = int(input("请输如爬取量:"))
    Main(i_d,n)