# Zhengzhou Restaruants analysis based on meituanAppSpider

Reference: https://github.com/hahaha108/meituanAppSpider

美团APP爬虫，可获取指定城市范围内所有美食店铺信息，包含店铺名称、类别、评分、所属片区、经纬度、详细地址、优惠套餐情况、营业时间、联系电话、累计售出份数、餐厅简介、特色菜......
<br>
可指定存储方式，有txt，csv 数据库2种方式可供选择

## 一、使用方法
可参照ZhengZhou_Restaurant_Meituan.ipynb<br>


## 二、注意事项
1.默认设置有随机2~5秒爬取间隔，建议不要修改<br>
2.若有需要文件存储名称、路径以及数据库设置项可在settings.py中修改<br>
3.默认爬取城市为郑州，由于美团APP的api中城市信息根据id传输，若要修改城市，只需修改spider_develop.py下base_url中city/后面的数字即可
```python
http://api.meituan.com/group/v4/deal/select/city/73/cate/1?sort=solds&hasGroup=true&mpt_cate1=1&offset={0}&limit=100
```
1为北京，10为上海，20为广州，30为深圳，73为郑州, 253为襄阳，其他的可抓包获取

## 三、结果
<br>
郑州美食偏好情况分析：<br>
1.最爱牛肉、牛肉丸、三文鱼、豆腐、水果
![](https://i.imgur.com/0IVWR6E.jpg)
<br>
