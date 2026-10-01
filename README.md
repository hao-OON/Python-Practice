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



### RagChat/

一个"先查资料，再回答"的问答程序。你问一句，它先去你自己的资料（QuotesCrawler 爬下来的名言和作者信息）里找相关的话，再把这几句话交给 AI，让 AI 只根据它们回答；资料里没有，它就说没有。

模块：requests，还有 DeepSeekChat 里用过的 open() 读 key。

新碰到的概念：

- RAG（检索增强生成）：先检索、再生成，让 AI 基于给定的资料回答，而不是凭自己的记忆瞎编。
- system 和 user 两种角色：system 用来定规则（只依据资料、资料里没有就直说），user 用来放资料和问题。
- 提示词约束：用规则把 AI 框住，防止它自由发挥、乱补内容。
- 关键词检索：现在用的是最笨的办法——你输入的整句话要原样出现在资料里才算命中，再按出现次数占全文的比例排序，取前三条拼成资料。

在运行前要在 RagChat 所在目录创建 deepseek_key.txt 文件，然后准备一个自己的 key，并把它复制到创建的文件里。

另外要先运行一次 QuotesCrawler 生成两个 json 文件。

```
cd RagChat
python main.py
```

在写这个项目的过程中，我遇到的最大的问题是现在的关键词检索带来：一是只要我换一种说法（用同义词、换个问法），检索就可能一条都找不到，AI 明明有资料，也只能回答"资料里没有相关内容"；二是排序只看出现次数占比，不看句子本身讲的是什么，所以排在最前面的不一定就是最相关的那条。这让我明白，检索这一层的好坏直接决定了最后回答的质量，光靠调提示词是补不回来的。