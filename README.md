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