# 專題實作後端 
## (尚未解決需思考的問題)
> PAGE_SIZE 跑掉的問題
> 爬蟲的精確度以及資料過濾
> 資料庫欄位設定以及資料表的連接
> 主鍵的設定
> json的顯示方式
> 搜尋的功能
> SQL injections/ use input validation
###### tags: `專題`




## 使用環境前置作業
參考：https://github.com/twtrubiks/django-transactions-tutorial
> install django 
> install PyMySQL
> install mysqlclient

## 資料庫連接出錯排除

匯入語法參考網址
>https://www.itread01.com/lfepy.html

資料匯入語法:
![](https://i.imgur.com/Y8XHchy.png)
![](https://i.imgur.com/XnFRmUE.png)

1. > ### 錯誤訊息 **(Error Code 1209)**
```
Error Code: 1290. The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
```

可以透過my.ini進行修改(參考網站內的修改)

解決方式參考:https://ithelp.ithome.com.tw/articles/10197804?sc=rss.qu

# 


2. > ### 錯誤訊息 **(Error Code 1261)**

![](https://i.imgur.com/lPFyLZS.png)

解決方式:要注意最後一行後還有沒有空白!!

# 

3. > ### 錯誤訊息 **(Error Code 1062)**

![](https://i.imgur.com/eSGun8l.png)

主鍵有相同，這個部分還要想辦法改進

4. > ### 錯誤訊息 **(Error Code 1262)**
![](https://i.imgur.com/PyKaU23.png)

可能資料裡有多出的逗號，要在資料裡檢查有沒有多出並刪除

## 建立超級使用者 
```
python manage.py createsuperuser
```

## ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑2019/05/14進度 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

## 修改顯示資訊

透過下列方式，可以修改要顯示的範圍(要對應到資料庫)
![](https://i.imgur.com/J5K18E7.png)
## 

## 序列化

參考網站:
https://www.cnblogs.com/iiiiiher/articles/9170572.html

https://docs.djangoproject.com/en/2.2/ref/contrib/gis/serializers/

http://www.liujiangblog.com/course/django/171

> ### 第一種
views:
![](https://i.imgur.com/AvOJcvc.png)

自己創一個serializers:
![](https://i.imgur.com/ZMHiL4P.png)

結果
![](https://i.imgur.com/tFP1kUU.png)


> ### 第二種
views:
![](https://i.imgur.com/MWUno4T.png)

template/index.html:
![](https://i.imgur.com/15poMdS.png)

![](https://i.imgur.com/L590TWD.png)



## 使用restframework(在分支restframework下)

### ---Serializers.py
這裡的HyperlinkedModelSerializer，是設定物件關聯性
>參考資料:https://www.atjiang.com/django-rest-tut5-relationships-and-hyperlinked-apis/

![](https://i.imgur.com/ca08rbB.png)

### ---Views.py
> 使用ViewSet來設定

![](https://i.imgur.com/NMboaaA.png)
![](https://i.imgur.com/vuLYnJd.png)

### ---Viewset.py
> 為了分類，建造一個viewset，將上面的動作做在viewset中

![](https://i.imgur.com/4sS3CBV.png)

> 然後設定Urls




### ---Urls.py
> 利用Router，我們可以快速設定網址
> 定義一個router，他的網址位置是data，網頁內容是DataViewSet

```
router = DefaultRouter()
router.register(r'data',DataViewSet)
```

![](https://i.imgur.com/7ipjMPZ.png)


![](https://i.imgur.com/t4dQxVh.png)

## 授權

在viewset中，使用IsAuthenticated
![](https://i.imgur.com/2hdIxv1.png)

引入登入頁面URL
![](https://i.imgur.com/UTuaqpq.png)

## 解析 Parsers

> 參考網站:http://www.django-rest-framework.org/api-guide/parsers/#parsersr

讓你的Content-Type只接受某種類型
通常如果沒有特別去設定 ，一般預設是使用 application / x-www-form-urlencode


![](https://i.imgur.com/m4CmFsx.png)

全域設定方式
```
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}
```
![](https://i.imgur.com/tJLyTbm.png)

區域設定(設定在自己想要的view上)

![](https://i.imgur.com/JbbP5WN.png)


## 自行設定get , post 所需的授權

> ### get 新增下列內容
> 1.get_permissions
> 2.status
> 3.def list
> 4.context,many

![](https://i.imgur.com/4WPioYb.png)



#### 1.get_permisssions

繼承下面方法，會透過return來回傳permission
![](https://i.imgur.com/hWKMTke.png)

所以可以透過下面修改，讓使用者要進行(create的時候，要認證)
![](https://i.imgur.com/WE7DvQ7.png)


#### 實際get方法(list)

繼承list方法
![](https://i.imgur.com/5A2LD6c.png)

--mixins.py
![](https://i.imgur.com/7QKSe1i.png)

#### status

參考網站:https://www.django-rest-framework.org/api-guide/status-codes/

> 用來定義http，增加可讀性

![](https://i.imgur.com/MCpogzx.png)

#### context / many

> 因為我們使用的是HyperlinkedModelSerializer，所以需要回傳一個request

![](https://i.imgur.com/iM7GWPs.png)

> 然後加上request的傳送

![](https://i.imgur.com/Z9TRK2v.png)

> 而many則是敘述該物件是多個還是單個

![](https://i.imgur.com/4836Uf6.png)

## 

> ### post
> 預設@permission_classes都會去呼叫get_permission這個函式，所以我們可以透過複寫他，來操作權限得使用


![](https://i.imgur.com/zmIHfuD.png)

## 連接css

![](https://i.imgur.com/rIH8jjZ.png)

![](https://i.imgur.com/3VMtYM0.png)

## detail的使用

> 新增一個detail方法，去分配每個id的url

--view.py配置
![](https://i.imgur.com/T2lcXCt.png)

--url.py配置
![](https://i.imgur.com/reNZm9p.png)

--detail.html配置
![](https://i.imgur.com/NbNC3eS.png)

## 將主頁和小頁分開
![](https://i.imgur.com/JAN1SLC.png)


## Raw SQL 

因為rest framework改版後，捨棄@list_route和@detail_route
改使用action，下面是action詳細介紹
![](https://i.imgur.com/hcflJcD.png)

```
@action(methods=[GET or POST], detail = True)
```
而我們要使用Raw SQL，所以先在models下建立函式
![](https://i.imgur.com/s7Abc5r.png)

然後再在viewset下新增一個方法，被action繼承

![](https://i.imgur.com/XW4Mwlg.png)

結果
![](https://i.imgur.com/Ul5iTFU.png)


## Prevent SQl injection(還未解決use input validation)

在使用Raw SQL時，會有SQL injection的問題，為了避免被使用SQL攻擊，我們可以參考

關於Parameter的說明
:https://stackoverflow.com/questions/4892166/how-does-sqlparameter-prevent-sql-injection

django官網參考範本:
https://docs.djangoproject.com/en/2.1/ref/models/querysets/


但最好的方法還是加上驗證碼，因為這種方式只能防護SQL injections，但如果是其他攻擊，例如:xss，就無法防護



![](https://i.imgur.com/oHxEdix.png)



![](https://i.imgur.com/5p6kFya.png)

### 2019/5/21改進

else原本會找不到東西，呈現not found狀態，於是現在不使用資料庫搜尋的方法，而是改使用下面方法

找不到就回傳全部訊息(可能可以把前端設計成搜尋時，如果有多個資料，就是找不到)
![](https://i.imgur.com/6uDeLxm.png)


## ngrok 測試API用

**下載方式:**
https://dashboard.ngrok.com/get-started

**教學:**
https://www.youtube.com/watch?v=GCIW-2RTcFY&t=19s

**使用注意:**
因為預設為不允許，所以在這裡把它改成允許存取
![](https://i.imgur.com/xkitlmS.png)

## __str__ 

可以利用__str__來重新設定物體字串

![](https://i.imgur.com/9uC763O.png)

我們進入shell模式測試，原本的亂碼變成了title

![](https://i.imgur.com/TWmyNj1.png)

## 新增delete的方法
 
 ![](https://i.imgur.com/YTFsZ5Y.png)

## 下次預計目標，使用detail重構GET/POST權限

detail重構get/post/put
-> 參考網址:https://www.django-rest-framework.org/tutorial/2-requests-and-responses/

建立樹根(endpoint)
-> 參考網址:https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/

REST URL
-> 參考網址:https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

# 嘗試使用generics.RetrieveAPIView已ModelView的除錯

使用ModelView時，因為它包含CRUD，所以在想要限制用RetrieveAPIView時，會出現循環輸入url的狀況

> 而我們現在嘗試一開始就用gernerics.RetrieveAPIView

使用CouponList來操作看看

--view.py
![](https://i.imgur.com/oBMIiKE.png)

--url.py
![](https://i.imgur.com/vsP1jWf.png)

所以我們可以得知，RetrieveAPIView在url中需要<指定項目>來抓取項目

如果我們使用lookup_field
![](https://i.imgur.com/uDHLNwr.png)

會出現
![](https://i.imgur.com/rY91CFS.png)

這是因為原先設定中，是以<pk>連結
![](https://i.imgur.com/3cNp4rb.png)

--url.py
![](https://i.imgur.com/dlUWDBi.png)

如果使用coupon_id，要改成
--url.py
![](https://i.imgur.com/7lH03fN.png)

## 使用generics.ListAPIView

在Coupon的設計上，我們只有我們自己可以新增和刪除內容，所以我們選擇List，讓使用者只能使用get

![](https://i.imgur.com/3FSH21B.png)

而在url的設定如下
![](https://i.imgur.com/B1lQG9m.png)

## 判斷create的user_id和user_name是否重複

判斷user_name是否重複
### --model.py
藉由讀取使用者輸入的user_name，設立一個result來判斷資料庫是否有重複資料
![](https://i.imgur.com/ZUecYQX.png)

藉由讀取使用者輸入的user_id，設立一個result來判斷資料庫是否有重複資料
![](https://i.imgur.com/DOyl75t.png)


### --view.py

藉由讀取使用者輸入的id,name(self.get_objcet())，以及實際將值，傳到--model.py來判斷，再回傳看看是否有重複，重複的話跑出提醒訊息，沒有重複就執行create

> self.get_object()是一個class，可用.user_id來呼叫他的user_id


![](https://i.imgur.com/GniDr9N.png)

![](https://i.imgur.com/i00VVcZ.png)

## api_root和HyperlinkedModelSerializer

> api_root:
> 可以把他想成一個根目錄，可以藉由它連結到其他各個子目錄，下圖中我們可以發現是以超連結做關聯，而不是PK做關聯

reverse:反向解析尋找url.py中的鳴子


***程式內容對照***
![](https://i.imgur.com/llCPuyQ.png)



***實際運作如下***
![](https://i.imgur.com/2a0UI2N.png)

***url.py內容***
![](https://i.imgur.com/P3R1dv5.png)


可參考網站:
https://www.jianshu.com/p/0489c309e88a

https://www.bookstack.cn/read/django-rest-framework-api-guide/api-guide-reverse.md

## ViewSet ＆ Routers

> 我們可以使ViewSet來簡化我們上面所寫到的Detail,List，將他們兩個自動包含到一個ViewSet裡，而api_root則以Router自動生成，讓我們可以專心在如何定義要傳遞的資料以及傳遞方式


我們在資料夾新增一個viewset.py的資料

### --viewset.py
***import:***
![](https://i.imgur.com/3OGcsGn.png)

***關於Coupon***
只要寫兩行，他就可以自動包含detail和list的功能，而使用**ReadOnlyModelViewSet**，可以自動設定只能讀取，不用在繁雜的設定其他東西
![](https://i.imgur.com/Lp1JgPD.png)


***關於User***
這裡我還在思考該如何設計，為了怕使用者可以藉由delete/put/patch刪除(更新)其他使用者資料，我們使用mixins的方法，來定義他只能做什麼

> 差異:
> put -> PUT 比較正確的定義是 Replace (Create or Update) ，存在就複寫，不存在就新增
> patch -> 部分更新
 
而為了避免使用者ID和名稱相同，我們依舊可以改寫create的判斷方式，與上面所用方式一樣就不贅述
![](https://i.imgur.com/smYThuc.png)
![](https://i.imgur.com/n6HLxPQ.png)

***關於--url.py***

我們使用預設的Routers，它會自動生成api_root，並只要透過register註冊viewset，就可以自動做出符合REST的url

Routers的參考:https://www.django-rest-framework.org/api-guide/routers/

![](https://i.imgur.com/Ql8ajDr.png)
