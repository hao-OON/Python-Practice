# Python Practice

我在学 Python 过程中写的小程序集合。



## 里面有什么



### MyOne.py

一个倒计时程序，算出距离 2027 年 3 月 1 日还有多少天、小时、分钟、秒。

用到 datetime 模块。



### NoteBook/

一个命令行学习记事本，可以记录每天学的内容、自动打上时间戳，也可以查看历史记录。

记录保存在本地文件里。



### GitHubStats/
一个从 GitHub 获取某个人的全部仓库列表的程序，并且把它存入repos.json文件里。

用到 requests，json，datetime 模块。

运行该程序：

```
cd GitHubStats
python github_stats.py
```



### DeepSeekChat/
一个调用deepseek-flash的程序，可以直接在命令行里和它进行带着记忆的连续对话。

用到 requests 模块，try/except 语句，open() 函数。

运行该程序：

在运行前要在DeepSeekChat所在目录创建deepseek_key.txt文件，然后准备一个自己的key，并把它复制到
创建的文件里。

```
cd DeepSeekChat
python deepseek_chat.py
```



### BookCrawler/
一个可以爬取books.toscrape.com中1000本书的程序，并把它们存入book_crawler_json.json文件里。

用到了 urljoin 函数，requests，bs4模块。

运行该程序：

```
cd BookCrawler
python book_crawler.py
```

在写这个项目的过程中，我遇到的最大的问题是url的拼接，因为每一个循环的下一页的地址不一样，所以拼接的基准也不一样，然后我查了 urljoin 的文档，判断出了基准应该跟着当前页走，解决了这个问题。在最后一页的时候，返回的下一页的地址的值为空，外层循环看见空，最终结束循环。



### QuotesCrawler/

一个可以爬取quotes.toscrape.com中所有名言的程序，并且把作者去重后，进一步爬取每位作者的信息，分别存入quotes_crawler_json.json和quotes_author_json.json文件里。

用到了 urljoin 函数，requests，bs4，json 模块。

运行该程序：

```
cd QuotesCrawler
python quotes_crawler.py
```

在写这个项目的过程中，我遇到的最大的问题是作者去重，因为同一个作者会在很多页里重复出现，如果不加判断就去访问作者页，同一个作者就会被重复爬很多遍。一开始我用作者的名字去重，但是其中会遇到同一个名字在两个网页会用微小差异的问题，所以我改成了判断这个作者的网址是不是已经抓过了，抓过就跳过，最终每个作者只爬一次。