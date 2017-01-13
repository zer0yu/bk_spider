### 百度百科人物信息爬虫

针对百度百科人物信息的聚焦爬虫。

使用示例如下：

```markdown
~/Desktop/info_spider » python zspider.py --help                     
Usage: spider.py [OPTIONS]
  _________  ____ ___ ____  _____ ____  
 |__  / ___||  _ \_ _|  _ \| ____|  _ \ 
   / /\___ \| |_) | || | | |  _| | |_) |
  / /_ ___) |  __/| || |_| | |___|  _ < 
 /____|____/|_|  |___|____/|_____|_| \_\
 Version 1.0 by
  zeroyu mail:zeroyu.xyz@gmail.com
Options:
  --version
  --count INTEGER                 需要爬取信息的数目
  --obj [sc_zh|star_zh|star_korea|em_zh|so_zh|his_zh|vir_w|ec_world|news|athlete|cartoon]
                                  设置爬虫对象
  --output [xls|sql]              数据输出后保存的位置
  --help                          Show this message and exit.
```

本项目只支持python2.7（以后就转python3啦）

依赖：

```markdown
pip install -r requirements.txt
```

