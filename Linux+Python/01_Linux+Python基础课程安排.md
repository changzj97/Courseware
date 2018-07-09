---
title: 01_Linux+Python基础课程安排
tags: Linux+Python
notebook: Linux+Python(Elit_ class)
---

[toc]


# 目标
- 明确第一个月课程内容

# 课程清单
| 序号 | 内容 | 目标 |
| -----| :-----:|-----:|
| 01 | Linux基础| 让大家对Ubuntu的使用从很**陌生**达到**灵活操作** |
| 02 | Python基础| 涵盖Python基础知识，让大家掌握基础的编程能力 |
| 03| Python面向对象| 介绍Python的面向对象开发，为开发大型项目做好铺垫和准备 |
| 04|项目实战| 应用学习过的知识，编程实战，完成第一个Python小项目 |

# 分享（一个合格的程序猿/媛）
- 你应该会翻墙、会谷歌、会把妹、会搞基

> 会翻墙

![选区_003](https://i.loli.net/2018/06/26/5b322aa96a367.png)
![选区_005](https://i.loli.net/2018/06/26/5b322b4d6e302.png)


> 会谷歌

![选区_007](https://i.loli.net/2018/06/26/5b322bf25d506.png)
![选区_008](https://i.loli.net/2018/06/26/5b322c1c2f1e1.png)

> 外面的'师姐'很精彩

![选区_006](https://i.loli.net/2018/06/26/5b322bae8e7dc.png)

> 会把妹

![选区_009](https://i.loli.net/2018/06/26/5b322c75db290.png)

> 会臭不要脸

![选区_010](https://i.loli.net/2018/06/26/5b322c9be81a8.png)

![选区_011](https://i.loli.net/2018/06/26/5b322d01a9684.png)

**醒来以后**

![选区_012](https://i.loli.net/2018/06/26/5b322d2556d86.png)

**你知道爬虫吗?做一个爬虫机器人+AI美女识别机如何?**
是不是有很多（污）的图片
![选区_013](https://i.loli.net/2018/06/26/5b322d4f47303.png)

> 会搞基

![选区_014](https://i.loli.net/2018/06/26/5b322d7cc5af3.png)

![Image](https://i.loli.net/2018/06/26/5b322dd158a52.gif)


> 你知道世界上最大的同性交友网站吗?

![选区_015](https://i.loli.net/2018/06/26/5b322dee98ba0.png)


# 最后正经一把:冰冻三尺非一日之寒，入木三分非一日之功

![9d891ca8f1774785897adad0d63771c9](https://i.loli.net/2018/06/26/5b322e8141274.jpeg)


# 仰望星空还要脚踏实地

![选区_016](https://i.loli.net/2018/06/26/5b322f1f430db.png)

> 你可以憧憬，但是不要应付任何事情，因为，你不知道，机会将要在何时来临。在这之前。你必须全力以赴。因为，机会只留给有准备的人。

![选区_017](https://i.loli.net/2018/06/26/5b322fca812e8.png)

# 需要做的几件事：
- 1. 工作日志/周志邮箱:wengwenyu888@aliyun.com
(注释:所有邮件,请抄送学院邮箱)

> 1. 整理好的知识和当天所有的课后练习的截图(shutter)
> 2. 什么地方看了视频以后还是听不懂


- 2. 技术博客:简书(请每位同学注册一个简书账号)

> 每周一篇

- 3. 印象笔记账号(务必每个同学到印象笔记的官网个人资料里面修改为真实资料,尤其是用户名)

> 找班长

---------

# 牛刀小试 — Linux
```
- 不积跬步，无以至千里;不积小流，无以成江海。
```

## 一、单选题



- 1.按照Ubuntu版本发布规律，2013年04月发行的版本，版本号应该是(    )
    A. 13.04	B. 13.02	C. 13.06	D. 12.08

- 2.Linux系统是参照(    )系统演变而来的
    A.unix	B.windows	C:Android	D.IOS

- 3.Redhat、Ubuntu、Debian都是基于（    ）系统的发行版
    A. Windows	B. linux	C. Anroid	D. ox

- 4.Ubuntu下安装管理软件包使用（    ）命令
    A.brew	B.yum	C.ls	D.apt-get

- 5.进入或切换目录使用( )命令
    A. ls   B. ln  C. cd  D. pwd

- 6.查看当前目录下的文件信息用( )命令
    A. ctrl+l  B. ls  C. cd  D. cd -

- 7.查看当前所在目录位置使用( )命令
    A. pwd  B. ls  C. ctrl+d  D. ctrl+f

- 8.用于复制文件命令（ ）
    A.rm		B.mv	C.cp			D.ctrl+c

- 9.下面哪个Linux命令可以一次显示一页内容（ ）
    A. pause 		B. cat 	C. more 		D. grep 

- 10.设置/test/a.txt属主有读写执行权限，属组，有读写，其他账户无权限（ ）
    A、 chmod 760 /test/a.txt		
    B、 chmod 762 /test/a.txt
    C、 chmod 761 /test/a.txt		
    D、 chmod 777 /test/a.txt

- 11.如何删除/tmp下所有A开头的文件？( )
    A、rm -rf /tmp/A*		B、rm /tmp/A*
    C、rm -if /tmp/A*		D、rm -i /tmp/A*

- 12.mv命令不具备（  ）功能
    A、移动文件		B、查看	C、重命名		D、移动文件夹

- 13.如何创建g1 组( )
    A、 groupdel g1	B、 groupadd g1	C、 chmod g1		D、 chown g1

- 14.下面远程登录写法正确的是( )
    A、sh uname@127.0.0.1 	B、 ssh 127.0.0.1@uanme
    C、ssh uname@127.0.0.1	D、 scp uname@127.0.0.1

- 15.远程拷贝文件用的命令是( )
    A、cp 		B、 scp	C、 ssh		D、 tar

- 16.用于归档文件的命令是( )
    A、cp 		B、 tar	C、 ping		D、 sip

- 17.根目录用什么表示( )
    A、/	B、 //	C、 \	D、 home

- 18.搜索文件的命令为( )
    A、grep	B、 cd	C、 ls	D、 find

- 19.强制删除文件夹的命令是( )
    A、rm -rf		B、 rm -r		C、 rm -f			D、 rm

- 20.创建文件夹的命令是( )
    A、touch		B、 tar	C、 mkdir		D、 vi

- 21.搜索文件内容的命令为( )
    A、grep		B、 cd	C、 ls		D、 find

- 22.查看IP地址的命令是( )
    A、ps		B、 du	C、 ifconfig	D、 ping

- 23.查看进程的命令是( )
    A、ps -aux	B、 ping	C、 ifconfig	D、 df

- 24.修改文件权限的命令是( )
    A、chown	B、 chgrp	C、 chuser	D、 chmod

- 25.以下说法正确的是(  )
    A、cd表示进入某个文件夹	B、Touch表示创建一个文件夹
    C、mkdir表示创建一个文件	D、rm可以直接删除文件夹

- 26.下列不是重启命令的是（ ）
    A、reboot	B、shutdown -r now 	C、init 0	  D、init 6

- 27.要使用SSH服务器服务端需要安装（ ）
    A、apt -get			B、pip
    C、openssh-server 		D、openssh-client

- 28.下列说法正确的是（ ）
    A、检测整个磁盘空间使用du	B、检测目录所占用的磁盘空间使用df
    C、查看ip地址使用Ping		D、可以使用cal查看日历

- 29.下面关于查看进程信息的命令说法正确的是（ ）
    A、使用df可以查看进程信息		B、可以使用du查看进程信息  
    C、ps-aux可以查看进程信息		D、top跟显示进程无关


## 二、判断题

- 1.需要自动补齐当前命令后续的字符用tab键（  ）
- 2.显示文本文件内容可以用cat命令(    ) 
- 3.重定向 > 表示输出，会将内容重定向到文件末尾（ ）
- 4.用who命令查询当前登录的用户(   ) 
- 5.使用pwd可以查看当前目录所有文件（  ） 
- 6.tar -jxvf可以压缩打包文件（  ）
- 7.Linux中查找文件的命令是grep（   ）

## 三、简答题

* 什么是绝对路径，什么是相对路径？

* 什么是操作系统?
* 常见的linux发行版本?(三种)
* 单用户操作系统和多用户操作系统的区别?
* Linux的根目录是什么?
* /home目录是什么?
* Linux终端命令格式
* 命令ls –la 的效果是什么?
* 清屏的命令是什么?
* 放大和缩小窗口字体大小的操作是什么?
* 使用man时的操作键 b键的作用?
* 通配符[]表示什么?
* cd – 的含义?
* 如何递归创建目录?
* 重定向>和>>的区别?
* 写出关机的命令 三种?
* 写出重启的命令 三种?
* 用户权限rwx分别表示什么?全拼是什么?
* 如何更改文件权限?
* 退出当前登录用户的命令?
* 查看进程的详细状况的命令是什么?
* apt是什么?
* 安装跑小火车的命令是什么?
* Vim编辑器命令行模式下写出三种退出并保存的指令?
* Vim编辑器命令行模式下强制退出的指令?
* Vim编辑器如何复制多行

 
# 四、操作题
1、在你的桌面下新建01文件夹，在01文件夹下 在新建一个01.txt文件，在并01.txt文件输入一些内容。并且查看它。然后进行新建02文件夹
2、在桌面上创建test目录，在里面创建aa bb cc三个文件夹，在aa里创建hello文件，在bb里创建world文件夹，在cc里创建it.py

-------

1、在桌面上创建01文件夹、在文件夹里面创建一个1.txt 2.txt   在1.txt里面写入一些内容。并且把内容重定向到3.txt。在01文件下 创建bb/cc/dd/ff  目录 在dd/里面创建04.txt。并且以递归的方式删除bb/cc/dd/ff。然后在01文件下创建05.txt  写入很多字。以more的方式查看
2、rmdir 和 rm -r 的区别
3、ls -a 是干什么用的
4、重定向>和>>有什么区别

5、在桌面上新建一个 11/22/33/44文件夹  在33文件夹里面新建1.txt 2.txt 3.txt 4.html 5.py 6.doc  以通配符的形式把.txt的文件重定向到6.txt了。并且给4.html创建软硬连接。

6、在桌面上创建一个文件夹，名字为load，在load下面有一个文件夹为one,在two文件夹下面有一个文件夹为three文件夹。
7、根据第六题，在two目录下创建几个文件，名字分别为1.py  2.py  3.html  team  sun.c    
和几个目录，名字分别为a  b  c  d  ab  dc  abc
8、通过 通配符查找以.txt结尾的文件 
9、通过 通配符查找以tea开头的文件  


10、在桌面上新建一个02day文件夹、在文件里面新建一个11.txt  在11.txt里面写入 王淋 刘婷婷 安华峰  崔树 崔永元  王含青  王润泽
用grep 来搜索 姓王的同学 在用grep搜索除了王姓的同学并重定向到 12.txt  
在用grep搜索结尾为元的姓名，在重定向追加到12.txt里面

11、在桌面新建一个01文件夹、在里面创建一个02文件夹
在01文件下创建1.py 2.py 3.py 4.txt  6.c 通过通配符的形式把.py的文件cp到02文件下。在把02文件夹改名称03文件夹。在创建一个04/05/06文件夹,在把03文件夹移动到05文件下。在把03里面的2.py改成4.py


-------

如有疑问,请联系(如无备注姓名拒绝):
![webwxgetmsgimg](https://i.loli.net/2018/07/03/5b3a576440a0b.jpeg)




