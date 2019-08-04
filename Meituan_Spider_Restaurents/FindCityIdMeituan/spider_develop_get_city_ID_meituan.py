#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Define a MeituanSpider class allows you to fetch meituan
restaurants infos in haikou city.
'''

import csv
import json
import os

import requests
import pymysql

import random
import time

from pymongo import MongoClient
from py2neo import Graph, Node
from settings import headers,limit





class MeituanSpider_getCityId(object):
    '''
    MeituanSpider class allows you to fetch all data from meituan api website.
    :Usage:
    '''

    baseUrl = ("http://api.meituan.com/group/v4/deal/select/city/{0}/cate/1?"
                "sort=solds&hasGroup=true&mpt_cate1=1&offset={1}&limit={2}")
  

    #美团郑州地区美食爬虫
    def __init__(self, saveMode='csv'):
        print("Meituan Spider is ready")

    
    def run(self):
        city_id = 1 # begin from 1, until we find the target city id.
        i = 0
        acquiredCount = 0
        find_city = False
        while True:
            url = self.baseUrl.format(city_id, str(i*limit), limit)
            find_city = self.parse(url)
            if find_city:
                print("The target city ID is: {}".format(city_id))
                break
            else:
                city_id +=1 # move to check next city
                if city_id%10 == 0:
                    print(city_id)
                    print("------------------------------------------------------------")
                    
            time.sleep(random.randint(2,5))




    def parse(self,url):
        response = requests.get(url,headers=random.choice(headers))
        number = 0 # count the request fails
        while True:
            try:
                info_dict = json.loads(response.text)
                info_list = info_dict['data']
                if info_list:
                    break
                else: # empty page
                    if info_dict['paging']['count'] ==0: # invalid city ID
                        return False 
                    number += 1
                    if number >= 3: # move to next city if fail more than 3 times. means that this is an unvalid city id
                        return False
                    time.sleep(5)
                    print("error1")
                    print(url)
                    response = requests.get(url, headers=random.choice(headers))            
            except: # 403 forbidden error 
                number += 1
                if number >= 3:
                    return False
                time.sleep(5)
                print("403 forbidden error, will re-try")
                print(url)
                response = requests.get(url, headers=random.choice(headers))

        itemlist = []
        for info in info_list:
            # 纬度
            lat = info['poi']['lat']
            # 经度
            lng = info['poi']['lng']
            # stop when the long and lat far away from the target area
            if float(lat) < 33 or float(lat) > 36:
                return False
            if float(lng) < 112 or float(lng) > 115:
                return False
            # 【河南郑州经纬度】 经度：113.65 ， 纬度：34.76
            if float(lat) > 34 and float(lat) <35:
                if float(lng) > 112 and float(lng) <115:
                    print("We find the city ID!")
                    print(addr)
                    return True     
        return False


    def __del__(self):
        '''
        The deconstructor of MeituanSpider class.
        Deconstructs an instance of MeituanSpider, closes MongoDB database and
        files.
        '''
        print('>>>> Finish.')



# test:
if __name__ == '__main__':
    spider = MeituanSpider(saveMode='csv')
    spider.run()