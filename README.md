# Henan Food and Customer anaysis
Henan is one of the densely populated provices in China (around 95 million).

Goal: Help the operation of a new noodle restaruant, called 'Macaroni of Zhang grandpa' (张爷爷空心面), located in Zhengzhou, Henan.

#### Data resources:
1. **Public data**: Online information related to customer and multi restaruants based on dazhong and meituan app
2. **Private data**: Daily sales/operating data of Macaroni of Zhang grandp restaruant


This repo shows all analysis using public data, mainly related to the following three parts:
### Part 1: [Henan food Analysis](https://github.com/YiranJing/WebSpider-NLP-foodAnalysis/new/master/FoodAnalysis_NLP)
- Get information from meituan and dazhong app, incuding customer comments, average prive, tags etc (App Spider tech).
- Try to understand Henan customers appetite, food aersions, and consumption ability of food (data visualization and NLP).

### Part 2: [Macaroni of Zhang grandpa chain restaurants analysis](https://github.com/YiranJing/WebSpider-NLP-foodAnalysis/tree/master/FoodAnalysis_NLP/ZhangyeyeNoodleRestaurant)
There are more than 200 Macaroni of Zhang grandpa in China, and more than 10 of them on Meituan and Dazhong app.
- Build Meituan AppSpider to collect information of 'Macaroni of Zhang grandpa' chain restaurants
- Data visulaization and NLP model


### Part 3: Customer analysis using sales data
- Data visualization
- customer classification based on customer behavor and age.
- customer analysis related to customer churn, customer retention, rush hour etc.


## 重要结论（不断更新中）
1. 张爷爷空心面人均消费在20-30元之间，在郑州的其他面粉里属于定价较高的 （其他普遍在10-20元之间）
2. 价格低于35元，顾客并没有倾向于用美团消费。间接说明人均35元以内的一顿饭对郑州人来说并不贵。因为他们并没有特别积极通过美团获得折扣 
3. 味道食材赞和分量足是张爷爷空心面的竞争优势。
4. 番茄牛腩空心面很受欢迎。
5. 郑州人喜欢吃快餐和面试类，张爷爷空心面符合郑州人胃口
6. 免费wifi服务对顾客评分和订单数并无帮助。

## 结果（不断更新中）
### 郑州人饮食喜好
![](https://github.com/YiranJing/WebSpider-NLP-foodAnalysis/blob/master/plot/%E9%83%91%E5%B7%9E%E4%BA%BA%E9%A5%AE%E9%A3%9F%E5%96%9C%E5%A5%BD.png)

郑州美团一共有108个美食分类。这个图画了前三十。字体越大说明相关饭店在郑州数量越多。
<br>
从这个图可以看出郑州市人民喜欢
1. 快餐小吃类
2. 火锅烧烤类
3. 蛋糕甜品类 (包括果汁奶茶)
4. 面食类（包括米线，米粉，面条，烩面）
5. 自助类

张爷爷空心面属于快餐类和面食类。芙蕾小姐属于甜品蛋糕类，在郑州市场都很受欢迎

### 价格和上周订单数的关系
![](https://github.com/YiranJing/WebSpider-NLP-foodAnalysis/blob/master/plot/%E4%BB%B7%E6%A0%BC%E5%92%8C%E4%B8%8A%E5%91%A8%E8%AE%A2%E5%8D%95%E6%95%B0%E5%85%B3%E7%B3%BB.png)
从上图可以看出，
1. 当人均价格高于35元时，顾客更倾向于用美团消费价格 （更多的折扣）（平均每家店铺有接近或大于200单）
2. 当人均消费在20-35元时，顾客并没有特别倾向于美团消费 （本来价格就亲民，顾客不太在意通过美团享受折扣）（平均每家店铺低于100单）

结论：
因为张爷爷空心面是价格在20-35元之间的快餐，所以美团优惠未必在吸引顾客方面有特别明显的作用。

推测：
对于30元一下的快餐食品类，顾客更在意味道品质，而不是几块钱价格的优惠。
郑州人的消费水平来看， 30元一顿饭并不贵。

### 所属地区的平均价格
![](https://github.com/YiranJing/WebSpider-NLP-foodAnalysis/blob/master/plot/%E9%83%91%E5%B7%9E%E5%B8%82%E4%B8%8D%E5%90%8C%E5%9C%B0%E5%8C%BA%E7%9A%84%E6%B6%88%E8%B4%B9%E6%83%85%E5%86%B5.png)

### 平均价格和评分的关系
![](https://github.com/YiranJing/WebSpider-NLP-foodAnalysis/blob/master/plot/%E4%BB%B7%E6%A0%BC%E5%92%8C%E8%AF%84%E5%88%86%E7%9A%84%E5%85%B3%E7%B3%BB.png)
从上图可以看出：
1. 价格在20元到30元之间的小吃店基本都评分较高（4分以上）
2. 顾客对高价格的食物评分更加严苛：价格超过40元较难获得好的评价

结论
20-30元的价格定位比较符合郑州人的消费心理。所以张爷爷空心面在郑州地区有价格优势

### 郑州面馆小吃店的研究
![](https://github.com/YiranJing/WebSpider-NLP-foodAnalysis/blob/master/plot/%E9%9D%A2%E9%A6%86%E6%A6%82%E5%86%B5.png)
从这个图我们可以看出：
1. 价格低的订单少（炸酱面）, 价格较高的消费时顾客更积极使用美团优惠
2. 郑州市的面平均价格在10-20元之间
结论：
张爷爷空心面在郑州属于定价较高的面食（价格劣势）
价格高的面食相对而言，美团优惠可能会取得较好效果

### Free Wifi服务有必要么？
根据数据分析结果：
1. 1.	免费wifi服务并不能使顾客提高评分
2. 2.	有wifi服务的平均价格较高
3. 3.	没有wifi服务的店铺订单更多
结论：
提供免费wifi服务没必要
