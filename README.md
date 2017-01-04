### 百度百科人物信息爬虫

​	近期帮老师搞点事情顺便把这个课程作业完成，也顺便练一下手，为后面的项目的那个爬虫工程奠定些基础。

使用示例如下：

```markdown
~/Desktop/info_spider » python spider.py --help                     
Usage: spider.py [OPTIONS]
  _________  ____ ___ ____  _____ ____  
 |__  / ___||  _ \_ _|  _ \| ____|  _ \ 
   / /\___ \| |_) | || | | |  _| | |_) |
  / /_ ___) |  __/| || |_| | |___|  _ < 
 /____|____/|_|  |___|____/|_____|_| \_\
Options:
  --version
  --count INTEGER     需要爬取信息的数目
  --output [xls|sql]  数据输出后保存的位置
  --help              Show this message and exit.
```

本项目只支持python2.7（以后就转python3啦）

依赖：

```markdown
pip install -r requirements.txt
```

