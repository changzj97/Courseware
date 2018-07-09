---
title: git和github
tags: 
notebook: Linux+Python(Elit_ class)
---


[toc]


# 一、git基本使用

-----

## 1、什么是git
Git 是 Linux 发明者 Linus 开发的一款新时代的版本控制系统，那什么是版本控制系统呢？怎么理解？网上一大堆详细的介绍，但是大多枯燥乏味，对于新手也很难理解，这里我只举几个例子来帮助你们理解。
熟悉编程的知道，我们在软件开发中源代码其实是最重要的，那么对源代码的管理变得异常重要：
比如为了防止代码的丢失，肯定本地机器与远程服务器都要存放一份，而且还需要有一套机制让本地可以跟远程同步；
又比如我们经常是好几个人做同一个项目，都要对一份代码做更改，这个时候需要大家互不影响，又需要各自可以同步别人的代码；
又比如我们开发的时候免不了有bug，有时候刚发布的功能就出现了严重的bug，这个时候需要紧急对代码进行还原；
又比如随着我们版本迭代的功能越来越多，但是我们需要清楚的知道历史每一个版本的代码更改记录，甚至知道每个人历史提交代码的情况；
等等等类似以上的情况，这些都是版本控制系统能解决的问题。所以说，版本控制是一种记录一个或若干文件内容变化，以便将来查阅特定版本修订情况的系统，对于软件开发领域来说版本控制是最重要的一环，而 Git 毫无疑问是当下最流行、最好用的版本控制系统。

`` 工作原理：``
![a1a1294f-f20d-4be8-bbb8-47c8516014c4](https://i.loli.net/2018/05/28/5b0bc2eedf831.png)

- Workspace：工作区
- Index / Stage：暂存区
- Repository：仓库区（或本地仓库）
- Remote：远程仓库

``SVN与Git的最主要的区别？``

SVN是集中式版本控制系统，版本库是集中放在中央服务器的，而干活的时候，用的都是自己的电脑，所以首先要从中央服务器哪里得到最新的版本，然后干活，干完后，需要把自己做完的活推送到中央服务器。集中式版本控制系统是必须联网才能工作，如果在局域网还可以，带宽够大，速度够快，如果在互联网下，如果网速慢的话，就纳闷了。

Git是分布式版本控制系统，那么它就没有中央服务器的，每个人的电脑就是一个完整的版本库，这样，工作的时候就不需要联网了，因为版本都是在自己的电脑上。既然每个人的电脑都有一个完整的版本库，那多个人如何协作呢？比如说自己在电脑上改了文件A，其他人也在电脑上改了文件A，这时，你们两之间只需把各自的修改推送给对方，就可以互相看到对方的修改了。

------

## 2、git安装(Ubuntu)
```vim
sudo apt install git 
```

------

## 3、git命令列表查看
- 请在命令行里输入git，如果出现以下提示证明你已经安装成功了
![fd3a8ca8-abbd-4df5-a1c1-c76d7f04d38b](https://i.loli.net/2018/05/28/5b0bc6fd8c848.png)

------

## 4、git具体命令（常用）
``第一步，我们先新建一个文件夹，在文件夹里面新建一个文件``

![83d9f147-8904-4b57-b4a3-2de542939542 (1)](https://i.loli.net/2018/05/28/5b0c065505be2.png)

> 提示：在进行任何git操作之前，都要先切换到自己的git仓库目录，也就是先要切换到项目的文件夹目录下

`` 这时候我们先随便操作一个命令：``
```git
git status
```
![b5d71f03-8e5c-44f1-8845-a53f9e5e7f16](https://i.loli.net/2018/05/28/5b0c075002dcb.png)

> 提示：意思是当前目录还不是一个git仓库

### git init(初始化仓库)

> 这时候我们用到了第一个命令。代表初始化git仓库,输入git init之后会提示

![a501210e-a7db-45b6-91a7-56e241636400](https://i.loli.net/2018/05/28/5b0c07fb27abc.png)

> 可以看到初始化成功了，至此test目录已经是一个git仓库了

### git status(查看仓库状态)

git status  这个命令顾名思义就是查看状态，这个命令可以算是使用最频繁的一个命令了，建议大家没事就输入下这个命令，来查看你当前 git 仓库的一些状态。
紧接着我们输入 git status 命令,会有如下提示:

![f15a7315-082b-4771-b552-6839025c0f6a](https://i.loli.net/2018/05/28/5b0c0942ab8d9.png)

> 提示: 默认就直接在 master 分支，关于分支的概念后面会提，这时最主要的是提示 a.md 文件 Untracked files ，就是说 a.md 这个文件还没有被跟踪，还没有提交在 git 仓库里呢，而且提示你可以使用 git add <文件名> 去操作你想要提交的文件。

### git add(添加到暂存区)

上面提示 a.md 文件还没有提交到 git 仓库里，这个时候我们可以随便编辑下 a.md 文件，然后输入 git add a.md ，然后再输入 git status :
![e3c7c221-5eca-4585-b73a-07f77e358941](https://i.loli.net/2018/05/28/5b0c09b544f0f.png)

> 此时提示以下文件 Changes to be committed(要提交的变更) ， 意思就是 a.md 文件等待被提交，当然你可以使用 git rm --cached 这个命令去移除这个缓存。

### git commit(提交到仓库)

接着我们输入 git commit -m 'first commit' ，这个命令什么意思呢？ commit 是提交的意思，-m 代表是提交信息，执行了以上命令代表我们已经正式进行了第一次提交。
![f342e72e-086f-45f3-bc34-395bf523f2de](https://i.loli.net/2018/05/28/5b0c0a205873c.png)

### git log(查看所有产生的commit记录)

![e86042c4-7726-4efc-b0dc-c6c7ebb76f0b](https://i.loli.net/2018/05/28/5b0c0aa4829d1.png)

### git add&git commit

看到这里估计很多人会有疑问，我想要提交直接进行 commit 不就行了么，为什么先要再 add 一次呢？首先 git add 是先把改动添加到一个「暂存区」，你可以理解成是一个缓存区域，临时保存你的改动，而 git commit 才是最后真正的提交。这样做的好处就是防止误提交，当然也有办法把这两步合并成一步，不过后面再介绍，建议新手先按部就班的一步步来。

### git branch(分支)

branch 即分支的意思，分支的概念很重要，尤其是团队协作的时候，假设两个人都在做同一个项目，这个时候分支就是保证两人能协同合作的最大利器了。举个例子，A, B俩人都在做同一个项目，但是不同的模块，这个时候A新建了一个分支叫a， B新建了一个分支叫b，这样A、B做的所有代码改动都各自在各自的分支，互不影响，等到俩人都把各自的模块都做完了，最后再统一把分支合并起来。

执行 git init 初始化git仓库之后会默认生成一个主分支 master ，也是你所在的默认分支，也基本是实际开发正式环境下的分支，一般情况下 master 分支不会轻易直接在上面操作的，你们可以输入 git branch 查看下当前分支情况：

![6333a0b2-60f6-4454-998a-d6a1dfa20e05](https://i.loli.net/2018/05/28/5b0c0b215c636.png)

如果我们想在此基础上新建一个分支呢，很简单，执行 git branch a 就新建了一个名字叫 a 的分支，这时候分支 a 跟分支 master 是一模一样的内容，我们再输入 git branch 查看的当前分支情况：

![3132bea6-f34a-4dd0-99ee-eac78c1fe467](https://i.loli.net/2018/05/28/5b0c0b4de796f.png)

但是可以看到 master 分支前有个 * 号，即虽然新建了一个 a 的分支，但是当前所在的分支还是在 master 上，如果我们想在 a 分支上进行开发，首先要先切换到 a 分支上才行，所以下一步要切换分支：

### git checkout a(切换分支)

执行这个命令，然后再输入 git branch 查看下分支情况：
![3132bea6-f34a-4dd0-99ee-eac78c1fe467](https://i.loli.net/2018/05/28/5b0c0b97d7ee7.png)

可以看到当前我们在的分支已经是a了，这个时候 A 同学就可以尽情的在他新建的a分支去进行代码改动了。
那有人就说了，我要先新建再切换，未免有点麻烦，有没有一步到位的，有：

### git checkout -b a ( 这个命令的意思就是新建一个a分支，并且自动切换到a分支。)

### git merge （合并分支）

A同学在a分支代码写的不亦乐乎，终于他的功能完工了，并且测试也都ok了，准备要上线了，这个时候就需要把他的代码合并到主分支master上来，然后发布。git merge 就是合并分支用到的命令，针对这个情况，需要先做两步，第一步是切换到 master 分支，如果你已经在了就不用切换了，第二步执行 git merge a ，意思就是把a分支的代码合并过来，不出意外，这个时候a分支的代码就顺利合并到 master 分支来了。为什么说不出意外呢？因为这个时候可能会有冲突而合并失败，留个包袱，这个到后面遇到的时候再讲。

### git branch -d （删除）

有新建分支，那肯定有删除分支，假如这个分支新建错了，或者a分支的代码已经顺利合并到 master 分支来了，那么a分支没用了，需要删除，这个时候执行 git branch -d a 就可以把a分支删除了。

### git branch -D （强制删除）

有些时候可能会删除失败，比如如果a分支的代码还没有合并到master，你执行 git branch -d a 是删除不了的，它会智能的提示你a分支还有未合并的代码，但是如果你非要删除，那就执行 git branch -D a 就可以强制删除a分支。

### git tag

在客户端开发的时候经常有版本的概念，比如v1.0、v1.1之类的，不同的版本肯定对应不同的代码，所以我一般要给我们的代码加上标签，这样假设v1.1版本出了一个新bug，但是又不晓得v1.0是不是有这个bug，有了标签就可以顺利切换到v1.0的代码，重新打个包测试了。
所以如果想要新建一个标签很简单，比如 git tag v1.0 就代表我在当前代码状态下新建了一个v1.0的标签，输入 git tag 可以查看历史 tag 记录。

![efc41da8-d91e-4f17-b5ad-71e315e46314](https://i.loli.net/2018/05/28/5b0c0c93c53ec.png)

> 提示： 想要切换到某个tag怎么办？也很简单，执行 git checkout v1.0 ，这样就顺利的切换到 v1.0 tag的代码状态了。

------

# 二、git进阶使用
## 1、用户名和邮箱
我们知道我们进行的每一次 commit 都会产生一条 log，这条 log 标记了提交人的姓名与邮箱，以便其他人方便的查看与联系提交人，所以我们在进行提交代码的第一步就是要设置自己的用户名与邮箱。执行以下代码：
```vim
git config --global user.name "wengwenyu"
git config --global user.email "wengwenyu@aliyun.com"
```

![0206f451-2d10-4b14-8188-b78b3563e0ae](https://i.loli.net/2018/05/28/5b0c0d9514deb.png)

> 以上进行了全局配置，当然有些时候我们的某一个项目想要用特定的邮箱，这个时候只需切换到你的项目目录，以上代码把 --global 参数去除，再重新执行一遍就ok了。

------

## 2、alias别名
我们知道我们执行的一些 Git 命令其实操作很频繁的类似有：
```vim
git commit
git checkout
git branch
git status
```
这些操作非常频繁，每次都要输入完全是不是有点麻烦，有没有一种简单的缩写输入呢？比如我想直接输入以下命令代替：
```vim
git c
git co
git br
git s
```
是不是很简单快捷啊？这个时候就用到了 alias 了，翻译过来就是别名的意思，输入以下命令就可以直接满足以上的需求。
```vim
git config --global alias.co checkout # 别名 
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.br branch
```
当然以上别名不是固定的，你完全可以根据自己的习惯去定制，除此之外还可以设置组合，比如：
```vim
git config --global alias.psm 'push origin master'
git config --global alias.plm 'pull origin master'
```
之后经常用到的 git push origin master 和 git pull origin master 直接就用 git psm 和 git plm 代替了，是不是很方便？
另外这里给大家推荐一个很强大的 alias 命令，我们知道我们输入 git log 查看日志的时候是类似这样的：
```vim
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
```
![a0000183-487e-4001-807e-3b4cdea6010d](https://i.loli.net/2018/05/28/5b0c0e5b53114.png)
是不是比较清晰，整个分支的走向也很明确，但是每次都要输这么一大串是不是也很烦？这时候你就该想到 alias 啊：
```vim
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative"
```
这样以后直接输入 git lg 就行了。

-----


## 3、其他配置
当然还有一些其他有用的配置，默认情况下 git 用的编辑器是 vi ，如果不喜欢可以改成其他编辑器，比如我习惯 vim 。

```vim
git config --global core.editor "vim"  # 设置Editor使用vim
```

有些人纳闷我的终端怎么有各种颜色显示，自己却不是这样的，那是因为你们没有开启给 Git 输出着色，输入如下命令即可：
```vim
git config --global color.ui true
```

git config --global color.ui true

以上的配置基本就差不多了，默认这些配置都在 ~/.gitconfig 文件下的，你可以找到这个文件查看自己的配置，也可以输入 git config -l 命令查看。

------

## 4、diff&checkout&stashmerge&rebase

### diff

diff 命令算是很常用的，使用场景是我们经常在做代码改动，但是有的时候2天前的代码了，做了哪些改动都忘记了，在提交之前需要确认下，这个时候就可以用diff来查看你到底做了哪些改动，举个例子，比如我有一个 a.md 的文件，我现在做了一些改动，然后输入 git diff 就会看到如下：

![8a744929-3682-4f38-b20d-dea80ac87e85](https://i.loli.net/2018/05/28/5b0c1136ab7d2.png)

红色的部分前面有个** -** 代表我删除的，绿色的部分前面有个 + 代表我增加的，所以从这里你们能一目了然的知道我到底对这个文件做了哪些改动。
值得一提的是直接输入 git diff 只能比较当前工作区文件和缓存区文件差异，什么是缓存区？就是你还没有执行 git add 的文件。
当然跟暂存区做比较之外，他还可以有其他用法，如比较两次 commit 之间的差异，比较两个分支之间的差异，比较缓存区和版本库之间的差异等，具体用法如下：

```vim
git diff <$id1> <$id2>   # 比较两次提交之间的差异
git diff <branch1>..<branch2> # 在两个分支之间比较
git diff --staged  # 比较暂存区和版本库差异
```

### checkout


我们知道 checkout 一般用作切换分支使用，比如切换到 develop 分支，可以执行：
```vim
git checkout develop
```
但是 checkout 不只用作切换分支，他可以用来切换 tag，切换到某次 commit，如：
```vim
git checkout v1.0
git checkout ffd9f2dd68f1eb21d36cee50dbdd504e95d9c8f7
```
后面的一长串是commit_id，是每次commit的SHA1值，可以根据 git log 看到。

除了有“切换”的意思，checkout 还有一个撤销的作用，举个例子，假设我们在一个分支开发一个小功能，刚写完一半，这时候需求变了，而且是大变化，之前写的代码完全用不了了，好在你刚写，甚至都没有 git add 进暂存区，这个时候很简单的一个操作就直接把原文件还原：
```vim
git checkout a.md
```
这里稍微提下，checkout 命令只能撤销还没有 add 进暂存区的文件。

### stash

设想一个场景，假设我们正在一个新的分支做新的功能，这个时候突然有一个紧急的bug需要修复，而且修复完之后需要立即发布。当然你说我先把刚写的一点代码进行提交不就行了么？这样理论上当然是ok的，但是这会产品垃圾commit，原则上我们每次的commit都要有实际的意义，你的代码只是刚写了一半，还没有什么实际的意义是不建议就这样commit的，那么有没有一种比较好的办法，可以让我暂时切到别的分支，修复完bug再切回来，而且代码也能保留的呢？
这个时候 stash 命令就大有用处了，前提是我们的代码没有进行 commit ，哪怕你执行了 add 也没关系，我们先执行
```vim
git stash
```
你会发现此时暂存区已经有了一条记录。
这个时候你可以切换回其他分支，赶紧把bug修复好，然后发布。之后一切都解决了，你再切换回来继续做你之前没做完的功能，但是之前的代码怎么还原呢？
```vim
git stash drop
```
就把最近一条的 stash 记录删除了，是不是很方便？其实还有更方便的，你可以使用：
```vim
git stash pop
```

来代替 apply 命令，pop 跟 apply 的唯一区别就是 pop 不但会帮你把代码还原，还自动帮你把这条 stash 记录删除，省的自己再 drop 一次了，虽然更方便，但是使用起来也需要更加谨慎，为了验证你可以紧接着执行 git stash list 命令来确认是不是已经没有该记录了。

最后还有一个命令介绍下：
```vim
git stash clear
```
就是清空所有暂存区的记录，drop 是只删除一条，当然后面可以跟 stash_id 参数来删除指定的某条记录，不跟参数就是删除最近的，而 clear 是清空。

### merge & rebase
我们知道 merge 分支是合并的意思，我们在一个 featureA 分支开发完了一个功能，这个时候需要合并到主分支 master 上去，我们只需要进行如下操作：
```vim
git checkout master
git merge featureA
```
其实 rebase 命令也是合并的意思，上面的需求我们一样可以如下操作：
```vim
git checkout master
git rebase featureA
```
rebase 跟 merge 的区别你们可以理解成有两个书架，你需要把两个书架的书整理到一起去，第一种做法是 merge ，比较粗鲁暴力，就直接腾出一块地方把另一个书架的书全部放进去，虽然暴力，但是这种做法你可以知道哪些书是来自另一个书架的；第二种做法就是 rebase ，他会把两个书架的书先进行比较，按照购书的时间来给他重新排序，然后重新放置好，这样做的好处就是合并之后的书架看起来很有逻辑，但是你很难清晰的知道哪些书来自哪个书架。
只能说各有好处，不同的团队根据不同的需要以及不同的习惯来选择就好。

--------

## 5、解决冲突
假设这样一个场景，A和B两位同学各自开了两个分支来开发不同的功能，大部分情况下都会尽量互不干扰的，但是有一个需求A需要改动一个基础库中的一个类的方法，不巧B这个时候由于业务需要也改动了基础库的这个方法，因为这种情况比较特殊，A和B都认为不会对别人造成影响，等两人各自把功能做完了，需要合并的到主分支 master 的时候，我们假设先合并A的分支，这个时候没问题的，之后再继续合并B的分支，这个时候想想也知道会有冲突了，因为A和B两个人同时更改了同一个地方，Git 本身他没法判断你们两个谁更改的对，但是这个时候他会智能的提示有 conflicts ，需要手动解决这个冲突之后再重新进行一次 commit 提交。

冲突的地方由 ==== 分出了上下两个部分，上部分一个有 HEAD 的字样代表是我当前所在分支的代码，下半部分是一个叫 baidu_activity分支的代码，可以看到 HEAD 对 gradle 插件进行了升级，同时新增了一个插件，所以我们很容易判断哪些代码该保留，哪些代码该删除，我们只需要移除掉那些老旧代码，而且同时也要把那些 <<< HEAD、==== 以及 >>>>>>baidu_activity 这些标记符号也一并删除，最后进行一次 commit 就ok了。

------

# 三、github
## 1、githu是什么

gitHub是一个面向开源及私有软件项目的托管平台，因为只支持git 作为唯一的版本库格式进行托管，故名gitHub。

![3b9c2d25-e498-4388-91e0-b757b3945f53](https://i.loli.net/2018/05/28/5b0c1c119419e.png)

全球顶级科技公司纷纷加入 GitHub ，并贡献他们自己的项目代码
Google: https://github.com/google
苹果: https://github.com/apple
Facebook: https://github.com/facebook
Twitter：https://github.com/twitter
微软：https://github.com/microsoft
Square：https://github.com/square
阿里：https://github.com/alibaba
全球顶级开源项目都优先选择在 GitHub 上开源
Linux：https://github.com/torvalds/linux
Rails：https://github.com/rails/rails
Nodejs：https://github.com/nodejs/node
Swift：https://github.com/apple/swift
CoffeeScript：https://github.com/jashkenas/coffeescript
Ruby：https://github.com/ruby/ruby
全球顶级编程大牛加入GitHub
Linux 发明者 Linus Torvalds：https://github.com/torvalds

![c95f3654-47e2-41ce-bff7-e11459cbeb36](https://i.loli.net/2018/05/28/5b0c1c4e4f416.png)

python最优秀的第三方 requests作者  Kenneth大神：https://github.com/kennethreitz

![44529e9e-e62f-4493-a703-7d366dd849c7](https://i.loli.net/2018/05/28/5b0c1c81ef552.png)

------

## 2、注册github

1.先去 GitHub 官网「https://github.com」注册「Sign Up」个账号，注册页面如下：

![f4b63128-b3f5-4a88-aa0f-85635ae096aa](https://i.loli.net/2018/05/28/5b0c1caf78a30.png)

这个应该没啥说的，需要填用户名、邮箱、密码，值得一提的用户名请不要那么随便，最好取的这个名字就是你以后常用的用户名了，也强烈建议你各大社交账号都用一样的用户名，这样识别度较高，比如我的博客域名、GitHub、知乎等其他社交账号 ID 都是 wengwenyu 而且这个用户名以后在 GitHub 搭建博客的时候默认给你生成的博客地址就是 username.github.io ，所以给自己取个好点的用户名吧。

> 填好用户名、邮箱、密码紧接着到这一步：
![ba4f0a93-807f-4ba8-91a4-15d27d0dc217](https://i.loli.net/2018/05/28/5b0c1cdf349a0.png)

GitHub 有两种，一种是公开，这种是免费的，就是你创建的项目是开放的，所有人都能看得到；另一种是私有，这种是收费的，这种一般是很多企业在使用 GitHub 的私有仓库在托管自己的项目，这也是 GitHub 的一种盈利模式对于个人你就直接默认选择公开的就行了。

直接submit后就会见到如下界面:

![cbccd052-b57f-4ce0-a9a6-5117fa766e9b](https://i.loli.net/2018/05/28/5b0c1d0031ec4.png)

> 设置和完善你的github:

![951132eb-0517-47cb-bc20-dec8247f0b4e](https://i.loli.net/2018/05/28/5b0c1d2301495.png)

## 3、一些github概念
### Repository

仓库的意思，即你的项目，你想在 GitHub 上开源一个项目，那就必须要新建一个 Repository ，如果你开源的项目多了，你就拥有了多个 Repositories 。

### Issue

问题的意思，举个例子，就是你开源了一个项目，别人发现你的项目中有bug，或者哪些地方做的不够好，他就可以给你提个 Issue ，即问题，提的问题多了，也就是 Issues ，然后你看到了这些问题就可以去逐个修复，修复ok了就可以一个个的 Close 掉。

### star

这个好理解，就是给项目点赞，但是在 GitHub 上的点赞远比微博、知乎点赞难的多，如果你有一个项目获得100个star都算很不容易了！

### Fork

这个不好翻译，如果实在要翻译我把他翻译成分叉，什么意思呢？你开源了一个项目，别人想在你这个项目的基础上做些改进，然后应用到自己的项目中，这个时候他就可以 Fork 你的项目，这个时候他的 GitHub 主页上就多了一个项目，只不过这个项目是基于你的项目基础（本质上是在原有项目的基础上新建了一个分支，分支的概念后面会在讲解Git的时候说到），他就可以随心所欲的去改进，但是丝毫不会影响原有项目的代码与结构。

### Pull Request

发起请求，这个其实是基于 Fork 的，还是上面那个例子，如果别人在你基础上做了改进，后来觉得改进的很不错，应该要把这些改进让更多的人收益，于是就想把自己的改进合并到原有项目里，这个时候他就可以发起一个 Pull Request（简称PR） ，原有项目创建人就可以收到这个请求，这个时候他会仔细review你的代码，并且测试觉得OK了，就会接受你的PR，这个时候你做的改进原有项目就会拥有了。

### Watch

这个也好理解就是观察，如果你 Watch 了某个项目，那么以后只要这个项目有任何更新，你都会第一时间收到关于这个项目的通知提醒。

### Gist

有些时候你没有项目可以开源，只是单纯的想分享一些代码片段，那这个时候 Gist 就派上用场了！


## 4、创建自己的项目

``点击顶部导航栏的 + 可以快速创建一个项目，如下图：``
![f80977b5-6bff-425b-9ca6-bf5dd5db848d](https://i.loli.net/2018/05/28/5b0c1e3e8c1c9.png)

![4e48abb6-4823-4cf7-aa1b-264ed453e43d](https://i.loli.net/2018/05/28/5b0c1e50e6462.png)

## 5、github提交代码

### SSH

你拥有了一个 GitHub 账号之后，就可以自由的 clone 或者下载其他项目，也可以创建自己的项目，但是你没法提交代码。仔细想想也知道，肯定不可能随意就能提交代码的，如果随意可以提交代码，那么 GitHub 上的项目岂不乱了套了，所以提交代码之前一定是需要某种授权的，而 GitHub 上一般都是基于 SSH 授权的。
那么什么是 SSH 呢？
简单点说，SSH是一种网络协议，用于计算机之间的加密登录。目前是每一台 Linux 电脑的标准配置。而大多数 Git 服务器都会选择使用 SSH 公钥来进行授权，所以想要在 GitHub 提交代码的第一步就是要先添加 SSH key 配置。

### 生成SSH Key

Linux 与 Mac 都是默认安装了 SSH ，而 Windows 系统安装了 Git Bash 应该也是带了 SSH 的。大家可以在终端（win下在 Git Bash 里）输入 ssh 如果出现以下提示证明你本机已经安装 SSH， 否则请搜索自行安装下。

#### windows
> 可以去Google一下windows版本的git官网下载相应软件

![fa1ccd21-548d-4cf9-9049-74ebc4897211](https://i.loli.net/2018/05/28/5b0c203ef2f0e.png)


#### Linux版本
紧接着输入 ssh-keygen -t rsa ，什么意思呢？就是指定 rsa 算法生成密钥，接着连续三个回车键（不需要输入密码），然后就会生成两个文件 id_rsa 和 id_rsa.pub ，而 id_rsa 是密钥，id_rsa.pub 就是公钥。这两文件默认分别在如下目录里生成：
Linux/Mac 系统 在 ~/.ssh 下，win系统在 /c/Documents and Settings/username/.ssh 下，都是隐藏文件，相信你们有办法查看的。
接下来要做的是把 id_rsa.pub 的内容添加到 GitHub 上，这样你本地的 id_rsa 密钥跟 GitHub 上的 id_rsa.pub 公钥进行配对，授权成功才可以提交代码。

![9560014a-f40f-47ef-8a86-738f01284af1](https://i.loli.net/2018/05/28/5b0c208985b3b.png)

> github上添加SSH key：

![1c10f794-761d-416e-ad31-080f3a04134b](https://i.loli.net/2018/05/28/5b0c20b97aa66.png)

然后点击右上角的 New SSH key 按钮：

![1c10f794-761d-416e-ad31-080f3a04134b](https://i.loli.net/2018/05/28/5b0c20e21f832.png)

需要做的只是在 Key 那栏把 id_rsa.pub 公钥文件里的内容复制粘贴进去就可以了，Title 那栏不需要填写，点击 Add SSH key 按钮就ok了。
这里提醒下，怎么查看 id_rsa.pub 文件的内容？

```vim
cd ~/.ssh
cat id_rsa.pub
```

SSH key 添加成功之后，输入 ssh -T git@github.com 进行测试，如果出现以下提示证明添加成功了。

![6724067a-7446-4061-86ca-6b0a44c0b750](https://i.loli.net/2018/05/28/5b0c211bf2513.png)



### 提交代码

添加 SSH key 成功之后，我们就有权限向 GitHub 上我们自己的项目提交代码了，而提交代码有两种方法：

#### clone自己代码
我们以我在 GitHub 上创建的 test 项目为例，执行如下命令：

![9f16f180-b4e8-4b61-ae28-3bb919c7f724](https://i.loli.net/2018/05/28/5b0c218caf5ae.png)

```vim
git@github.com:wengwenyu888/test.git  
```
可以把 clone 命令理解为高级点的复制，这个时候该项目本身就已经是一个git 仓库了，不需要执行 git init 进行初始化，而且甚至都已经关联好了远程仓库，我们只需要在这个 test 目录下任意修改或者添加文件，然后进行 commit ，之后就可以执行：

```vim
git push origin master
```

进行代码提交，这种是最简单方便的一种方式。


#### 关联本地已有项目

如果我们本地已经有一个完整的 git 仓库，并且已经进行了很多次 commit ，这个时候第一种方法就不适合了。
假设我们本地有个 test2 的项目，我们需要的是在 GitHub 上建一个 test 的项目，然后把本地 test2 上的所有代码 commit 记录提交到 GitHub 上的 test 项目。
第一步就是在 GitHub 上建一个 test 项目，这个想必大家都会了，就不用多讲了。
第二步把本地 test2 项目与 GitHub 上的 test 项目进行关联，在本地切换到 test2 目录，执行如下命令：
```vim
git remote add origin  git@github.com:wengwenyu/test.git
```

什么意思呢？就是添加一个远程仓库，他的地址是 git@github.com:wengwenyu/test.git ，而 origin 是给这个项目的远程仓库起的名字，是的，名字你可以随便取，只不过大家公认的只有一个远程仓库时名字就是 origin ，为什么要给远程仓库取名字？因为我们可能一个项目有多个远程仓库？比如 GitHub 一个，比如公司一个，这样的话提交到不同的远程仓库就需要指定不同的仓库名字了。

#### 查看我们当前项目有哪些远程仓库
```vim
git remote -v
```

> 接下来，我们本地的仓库就可以向远程仓库进行代码提交了：

```vim
git push origin master
```

就是默认向 GitHub 上的 test 目录提交了代码，而这个代码是在 master 分支。


-----


# 四、团队合作
## 1、什么是分支
Git 相比于 SVN 最强大的一个地方就在于「分支」，Git 的分支操作简直不要太方便，而实际项目开发中团队合作最依赖的莫过于分支了，关于分支前面的系列也提到过，但是本篇会详细讲述什么是分支、分支的具体操作以及实际项目开发中到底是怎么依赖分支来进行团队合作的。
其实你们可以这么理解，你们几个人一起去旅行，中间走到一个三岔口，每条路可能有不同的风景，你们约定 3 天之后在某地汇聚，然后各自出发了。而这三条分叉路就可以理解成你们各自的分支，而等你们汇聚的时候相当于把你们的分支进行了合并。

## 2、分支基本常用操作
通常我们默认都会有一个主分支叫 master ，下面我们先来看下关于分支的一些基本操作：
### 新建一个叫develop的分支
```vim
git  branch develop
```
这里稍微提醒下大家，新建分支的命令是基于当前所在分支的基础上进行的，即以上是基于 mater 分支新建了一个叫做 develop 的分支，此时 develop 分支跟 master 分支的内容完全一样。如果你有 A、B、C三个分支，三个分支是三位同学的，各分支内容不一样，如果你当前是在 B 分支，如果执行新建分支命令，则新建的分支内容跟 B 分支是一样的，同理如果当前所在是 C 分支，那就是基于 C 分支基础上新建的分支。
### 切换到develop分支：
```vim
git checkout -b develop   
```
### 把develop分支推送到远程仓库：
```vim
git push origin develop    
```
> 如果你远程的分支想取名叫 develop2 ，那执行以下代码：
```vim
git push origin develop:develop2  
```
但是强烈不建议这样，这会导致很混乱，很难管理，所以建议本地分支跟远程分支名要保持一致。

### 查看本地分支

```vim
git branch  
```

### 查看远程分支
```vim
git branch -r  
```

### 删除本地分支
```vim
git branch -d develop    

git branch -D develop (强制删除)    
```
### 删除远程分支
```vim
git push origin :develop   
```
> 如果远程分支有个develop，而本地没有，你想把远程的develop分支迁到本地
```vim
git checkout develop origin/develop  
```
> 同样的把远程分支迁移到本地顺便切换该分支
```vim
git checkout -b develop origin/develop    
```




## 3、基本团队协作流程

一般来说，如果你是一个人开发，可能只需要 master、develop 两个分支就 ok 了，平时开发在 develop 分支进行，开发完成之后，发布之前合并到 master 分支，这个流程没啥大问题。
如果你是 3、5 个人，那就不一样了，有人说也没多大问题啊，直接可以新建 A、B、C 三个人的分支啊，每人各自开发各自的分支，然后开发完成之后再逐步合并到 master 分支。然而现实却是，你正在某个分支开发某个功能呢，这时候突然发现线上有一个很严重的 bug ，不得不停下手头的工作优先处理 bug ，而且很多时候多人协作下如果没有一个规范，很容易产生问题，所以多人协作下的分支管理规范很重要，就跟代码规范一样重要，以下就跟大家推荐一种我们内部在使用的一种分支管理流程 Git Flow。


## 4、git Flow

我们都知道, 在 git 的分支功能相对 svn 确实方便许多，而且也非常推荐使用分支来做开发. 我的做法是每个项目都有2个分支, master 和 develop. master 分支是主分支, 保证程序有一个 稳定版本, develop 则是开发用的分支, 几乎所有的功能开发, bug 修复都在这个分支上, 完成后 再合并回 master.
但是情况并不是这么简单. 有时当我们正在开发一个功能, 但程序突然出现 bug 需要及时去修复的时候, 这时要切回 master 分支, 并基于它创建一个 hotfix 分支. 有时我们在开发一个功能时, 需要停下来去开发另一个功能. 而且所有这些问题都出现 的时候, 发布也会成为比较棘手问题.
也就是说, git branch 功能很强大，但是没有一套模型告诉我们应该怎样在开发的时候善用 这些分支。于是有人就整理出了一套比较好的方案 A successful Git branching model, 今天我们就一起来学习下这套方案.
准确的说 Git Flow 是一种比较成熟的分支管理流程，我们先看一张图能清晰的描述他整个的工作流程：

![300fa96b-529d-42e5-a412-f869b5b7d08e](https://i.loli.net/2018/05/28/5b0c24f630df7.png)

第一次看上面那个图是不是一脸懵逼？跟我当时一样，不急，我来用简单的话给你们解释下。
一般开发来说，大部分情况下都会拥有两个分支 master 和 develop，他们的职责分别是：

### master
永远处在即将发布(production-ready)状态
### develop
最新的开发状态
确切的说 master、develop 分支大部分情况下都会保持一致，只有在上线前的测试阶段 develop 比 master 的代码要多，一旦测试没问题，准备发布了，这时候会将 develop 合并到 master 上。
但是我们发布之后又会进行下一版本的功能开发，开发中间可能又会遇到需要紧急修复 bug ，一个功能开发完成之后突然需求变动了等情况，所以 Git Flow 除了以上 master 和 develop 两个主要分支以外，还提出了以下三个辅助分支：
### feature
开发新功能的分支, 基于 develop, 完成后 merge 回 develop
### release
准备要发布版本的分支, 用来修复 bug，基于 develop，完成后 merge 回 develop 和 master第一次看上面那个图是不是一脸懵逼？跟我当时一样，不急，我来用简单的话给你们解释下。
一般开发来说，大部分情况下都会拥有两个分支 master 和 develop，他们的职责分别是：
### hotfix
修复 master 上的问题, 等不及 release 版本就必须马上上线. 基于 master, 完成后 merge 回 master 和 develop

什么意思呢？
举个例子，假设我们已经有 master 和 develop 两个分支了，这个时候我们准备做一个功能 A，第一步我们要做的，就是基于 develop 分支新建个分支：

```vim
git branch feature/A    
```

看到了吧，其实就是一个规范，规定了所有开发的功能分支都以 feature 为前缀。
但是这个时候做着做着发现线上有一个紧急的 bug 需要修复，那赶紧停下手头的工作，立刻切换到 master 分支，然后再此基础上新建一个分支：

```vim
git branch hotfix/B 
```

代表新建了一个紧急修复分支，修复完成之后直接合并到 develop 和 master ，然后发布。
然后再切回我们的 feature/A 分支继续着我们的开发，如果开发完了，那么合并回 develop 分支，然后在 develop 分支属于测试环境，跟后端对接并且测试的差不多了，感觉可以发布到正式环境了，这个时候再新建一个 release 分支：

```vim
git branch release/1.0  
```