---
title: 博客项目(Django版)项目
tags: Django
notebook: 7.0第五月 Python_web后端
---

[toc]


# 一、项目概述

## 项目运行环境
1. Python3.6+
2. Django 1.11
3. MySQL 5.7
4. 其他插件(图片处理、分页、验证码....)
## 项目详细功能介绍
### 前台功能
1. 项目首页展示
2. 轮播图
3. 博客推荐
4. 最新发布
5. 博客分类
6. 最新评论文章
7. widgets小插件
8. 搜索功能
9. 博客分类功能
10. 博客标签查询
11. 友情链接
12. 博客分页功能
13. 博客详细
14. 最新评论文章
15. 发表评论
16. 评论展示
17. 评论数
18. 阅读数
19. 登录功能
20. 注册功能
21. 邮箱验证功能
22. 注销功能
23. 页面模板
24. 标签云功能
25. 读者墙功能

### 后台功能
1. 用户维护
2. 权限管理
3. 博客分类维护
4. 标签维护
5. 友情链接
6. 轮播图维护

### 项目演示
项目演示
### 项目代码演示
代码展示

# 二、开发环境搭建

> 使用virtualenv 和 virtualenwrapper

1. MySQL 5.7

```vim
sudo apt install mysql-server mysql-client
```

2. 安装mysql驱动

```vim
pip install pymysql
```

3. 安装Django

```vim
pip install django==1.11
```



# 三、创建项目
## 创建项目和应用

- 创建项目

```vim
django-admin startproject django-blog
```

- 创建应用

```vim
python manage.py startapp userapp
python manage.py startapp blogapp
```


## 配置数据库

- 在settings中配置数据库

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_blog_db',
        'USER': 'root',
        'PASSWORD': 'wwy123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

## 创建数据库(执行迁移文件)

```python
python manage.py migrate
```

## 创建超级管理员
```python
python manage.py createsuperuser
```

# 四、创建数据模型

## USERAPP
###　USER(用户模型)

```django
from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser):
    nikename = models.CharField('昵称', max_length=20, default='')
```
> 提示：需要在settings配置文件中设置:AUTH_USER_MODEL = 'users.BlogUser'

### EMAIL(邮箱验证数据模型)

```django
class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name='验证码', max_length=50,default='')
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name="验证码类型", choices=(("register",u"注册"),("forget","找回密码"), ("update_email","修改邮箱")), max_length=30)
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        # 复数
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)
```
## BLOGAPP
### Banner(轮播图模型)
```django
class Banner(models.Model):
    title = models.CharField('标题', max_length=50)
    cover = models.ImageField('轮播图', upload_to='static/images/banner')
    link_url = models.URLField('图片链接', max_length=100)
    idx = models.IntegerField('索引')
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'
```

### Category(博客分类模型)
```django
class BlogCategory(models.Model):
    name = models.CharField('分类名称', max_length=20, default='')
    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'

    def __str__(self):
        return self.name
```

### Tags(标签模型)
```django
class Tags(models.Model):
    name = models.CharField('标签名称', max_length=20, default='')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name
```

### Blog(博客模型)
```django
class Post(models.Model):
    user = models.ForeignKey(BlogUser, verbose_name='作者')
    category = models.ForeignKey(BlogCategory, verbose_name='博客分类', default=None)
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    pub_date = models.DateTimeField('发布日期', default=datetime.now)
    cover = models.ImageField('博客封面', upload_to='static/images/post', default=None)
    views = models.IntegerField('浏览数', default=0)
    recommend = models.BooleanField('推荐博客', default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'
```

### Comment(评论模型)

```django
class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name='博客')
    user = models.ForeignKey(BlogUser, verbose_name='作者')
    pub_date = models.DateTimeField('发布时间')
    content = models.TextField('内容')

    def __str__(self):
        return self.content
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
```

### FriendlyLink(友情链接模型)

```django
class FriendlyLink(models.Model):
    title = models.CharField('标题', max_length=50)
    link = models.URLField('链接', max_length=50, default='')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
```

# 五、实现首页页面模板
## 创建模板文件夹
> 创建模板文件templates,并在settings.py中设置

```django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
## 配置静态文件路径

```django
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
```


# 六、创建首页路由

- 创建视图函数
```django
def index(request):
    return render(request, 'index.html',  {})
```
- 配置url
```django
url(r'^$', index, name='index' )
```
- 修改模板CSS　JS等静态文件的路径


# 七、实现幻灯片功能(Banner)

- 注册模型
```django
from blogs.models import Banner
admin.site.register(Banner)
```
- 编写views
```django
from .models import Banner

def index(request):
    banner_list = Banner.objects.all()
    ctx = {
        'banner_list': banner_list,    
    }
    return render(request, 'index.html',  ctx)
```

- 模板
```django
  <!-- banner 开始 -->
  <div id="focusslide" class="carousel slide" data-ride="carousel">
	<ol class="carousel-indicators">

    {% for banner in banner_list %}
    {% if banner.is_active %}
	  <li data-target="#focusslide" data-slide-to="{{banner.idx}}" class="active"></li>
    {% else %}
	  <li data-target="#focusslide" data-slide-to="{{banner.idx}}"></li>
    {% endif %}
    {% endfor %}

	</ol>
	<div class="carousel-inner" role="listbox">

    {% for banner in banner_list %}
    {% if banner.is_active %}
      <div class="item active">
      <a href="{{banner.link_url}}" target="_blank" title="{{banner.title}}" >
      <img src="{{banner.cover}}" alt="{{banner.title}}" class="img-responsive"></a>
      </div>
    {% else %}
      <div class="item">
      <a href="{{banner.link_url}}" target="_blank" title="{{banner.title}}" >
      <img src="{{banner.cover}}" alt="{{banner.title}}" class="img-responsive"></a>
      </div>
    {% endif %}
    {% endfor %}

	</div>
	<a class="left carousel-control" href="#focusslide" role="button" data-slide="prev" rel="nofollow">
     <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
     <span class="sr-only">上一个</span> </a>
  <a class="right carousel-control" href="#focusslide" role="button" data-slide="next" rel="nofollow">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">下一个</span> </a>
  </div>

  <!-- banner 结束 -->
```
# 八、实现博客推荐
- 注册模型
```django
from blogs.models import Banner,Post,BlogCategory,Tags
...
admin.site.register(BlogCategory)
admin.site.register(Tags)
admin.site.register(Post)
```
- 编写views
```django

# 视图函数 HTTPRequest
def index(request):
    banner_list = Banner.objects.all()
    recommend_list = Post.objects.filter(recommend=1)
    ctx = {
        'banner_list': banner_list,
        'recommend_list': recommend_list,      
    }
    return render(request, 'index.html',  ctx)
```
- 模板
```html
  <!-- 推荐开始 -->
  {% for post in recommend_list %}
  <article class="excerpt-minic excerpt-minic-index">
		<h2><span class="red">【推荐】</span><a target="_blank" href="/blog/{{post.id}}/" title="{{post.title}}" >{{post.title}}</a>
		</h2>
		<p class="note">{{post.content}}</p>
	</article>
  {% endfor %}
  <!-- 推荐结束 -->
```
# 九、实现最新发布
- 编写views
```django
# 视图函数 HTTPRequest
def index(request):
    ...
    post_list = Post.objects.order_by('-pub_date').all()[:10]
    ....
    ctx = {
        'banner_list': banner_list,
        'recommend_list': recommend_list,
        'post_list': post_list,
        
    }
    return render(request, 'index.html',  ctx)
```
- 模板
```django
  <!-- 最新发布的博客开始 -->

  {% for post in post_list%}

  <article class="excerpt excerpt-1" style="">
  <a class="focus" href="/blog/{{post.id}}/" title="{{post.title}}" target="_blank" ><img class="thumb" data-original="/{{post.cover}}" src="/{{post.cover}}" alt="{{post.title}}"  style="display: inline;"></a>
		<header><a class="cat" href="#" title="{{post.category.name}}" >{{post.category.name}}<i></i></a>
			<h2><a href="/blog/{{post.id}}/" title="{{post.title}}" target="_blank" >{{post.title}}</a>
			</h2>
		</header>
		<p class="meta">
			<time class="time"><i class="glyphicon glyphicon-time"></i>{{post.pub_date|date:'Y-m-d'}}</time>
			<span class="views"><i class="glyphicon glyphicon-eye-open"></i>{{post.views}}</span> <a class="comment" href="##comment" title="评论" target="_blank" ><i class="glyphicon glyphicon-comment"></i>{{post.comment_set.count}}</a>
		</p>
		<p class="note">


      {% autoescape off %}
          {{post.content | truncatechars_html:200}}
      {% endautoescape %}

    </p>
	</article>

  {% endfor %}


  <!-- 最新发布的博客结束 -->
```
# 十、实现博客分类功能
- 编写视图
```django
# 视图函数 HTTPRequest
def index(request):
    banner_list = Banner.objects.all()
    recommend_list = Post.objects.filter(recommend=1)
    post_list = Post.objects.order_by('-pub_date').all()[:10]
    blogcategory_list = BlogCategory.objects.all()

    ctx = {
        'banner_list': banner_list,
        'recommend_list': recommend_list,
        'post_list': post_list,
        'blogcategory_list': blogcategory_list,
    }
    return render(request, 'index.html',  ctx)
```
- 模型
```html
  <div class="title">
	<h3>最新发布</h3>
	<div class="more">
      {%for c in blogcategory_list%}
			  <a href="/category/{{c.id}}" title="{{c.name}}" >{{c.name}}</a>
			{% endfor %}
		</div>
  </div>
```

# 十一、实现最新评论功能
- 编写views
```django
 <ul>

                {% for post in new_comment_list %}
                    <li><a title="{{ post.title }}" href="#"><span class="thumbnail">
				<img class="thumb" data-original="/{{ post.cover }}"
                     src="/{{ post.cover }}"
                     alt="{{ post.title }}" style="display: block;">
			</span><span class="text">{{ post.title }}</span><span class="muted"><i
                            class="glyphicon glyphicon-time"></i>
				{{ post.pub_date }}
			</span><span class="muted"><i class="glyphicon glyphicon-eye-open"></i>{{ post.views }}</span></a></li>
                {% endfor %}


            </ul>
```
# 十二、实现搜索功能
- 编写views
```django
from django.views.generic.base import View
from django.db.models import Q
class SearchView(View):
    # def get(self, request):
    #     pass
    def post(self, request):
        kw = request.POST.get('keyword')
        post_list = Post.objects.filter(Q(title__icontains=kw)|Q(content__icontains=kw))

        ctx = {
            'post_list': post_list
        }
        return render(request, 'list.html', ctx)
```
- urls
```django
url(r'^search$', SearchView.as_view(), name='search'),
```

# 十三、实现友情链接
- 编写视图  (数据源)
```django
def index(request):
    ....
    friendlylink_list = FriendlyLink.objects.all()
    .....
```
- 模板
```django

        <div class="widget widget_sentence">
            <h3>友情链接</h3>
            <div class="widget-sentence-link">
                {% for friendlylink in friendlylink_list %}

                    <a href="{{ friendlylink.link }}" title="{{ friendlylink.title }}"
                       target="_blank">{{ friendlylink.title }}</a>&nbsp;&nbsp;&nbsp;
                {% endfor %}


            </div>
        </div>
```

# 十四、实现博客列表功能
- 编写views
```django
def blog_list(request):
    post_list = POST.objects.all()
    ctx = {
        'post_list': post_list,
    }
    return render(request, 'list.html', ctx)
```
- 编写路由
```django
url(r'^list$', blog_list, name='blog_list'),
```
- base.html
```html
<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="renderer" content="webkit">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{% block title %}知奇博客首页 {% endblock %}</title>
<meta name="keywords" content="">
<meta name="description" content="">


{% block custom_css %}{% endblock %}
<link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css">
<link rel="stylesheet" type="text/css" href="/static/css/nprogress.css">
<link rel="stylesheet" type="text/css" href="/static/css/style.css">
<link rel="stylesheet" type="text/css" href="/static/css/font-awesome.min.css">
<link rel="apple-touch-icon-precomposed" href="/static/images/icon.png">
<link rel="shortcut icon" href="/static/images/favicon.ico">

<script src="/static/js/jquery-2.1.4.min.js"></script>
<script src="/static/js/nprogress.js"></script>
<script src="/static/js/jquery.lazyload.min.js"></script>

</head>
<body class="user-select">
<header class="header">
<nav class="navbar navbar-default" id="navbar">
<div class="container">
  <div class="header-topbar hidden-xs link-border">
  	<ul class="site-nav topmenu">
  	  <li><a href="#" >标签云</a></li>
  		<li><a href="#" rel="nofollow" >读者墙</a></li>
  		<li><a href="#" title="RSS订阅" >
  			<i class="fa fa-rss">
  			</i> RSS订阅
  		</a></li>
  	</ul>
			 爱学习 更爱分享
  </div>
  <div class="navbar-header">
	<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#header-navbar" aria-expanded="false"> <span class="sr-only"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>
	<h1 class="logo hvr-bounce-in"><a href="#" title="知奇课堂博客"><img src="/static/images/201610171329086541.png" alt="知奇课堂博客"></a></h1>
  </div>
  <div class="collapse navbar-collapse" id="header-navbar">

	<ul class="nav navbar-nav navbar-left">
	  <li><a data-cont="知奇课堂博客" title="知奇课堂博客" href="/">首页</a></li>
	  <li><a data-cont="博客" title="博客" href="/list">博客</a></li>
	</ul>


  <ul class="nav navbar-nav navbar-right">
    {% if user.is_authenticated %}
    <li><a data-cont="用户" title="用户" href="#">欢迎，{{user.username}}</a></li>
    <li><a data-cont="注册" title="注册" href="/logout">注销</a></li>
    {% else %}
    <li><a data-cont="登录" title="登录" href="/login">登录</a></li>
    <li><a data-cont="注册" title="注册" href="/register">注册</a></li>
    {% endif %}
  </ul>

  </div>
</div>
</nav>
</header>

{% block content %}
{% endblock %}

<footer class="footer">
<div class="container">
<p>Copyright &copy; 2016.Company name All rights reserved.</p>
</div>
<div id="gotop"><a class="gotop"></a></div>
</footer>
<script src="/static/js/bootstrap.min.js"></script>
<!-- <script src="/static/js/jquery.ias.js"></script> -->
<script src="/static/js/scripts.js"></script>
</body>
</html>

```
# 十五、实现分页功能
- 安装包
```django
pip install django-pure-pagination
```
> 参考链接: https://github.com/jamespacileo/django-pure-pagination

```django
def blog_list(request):
    post_list = Post.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(post_list, per_page=1, request=request)
    post_list = p.page(page)
    ctx = {
        'post_list': post_list,
        
    }
    return render(request, 'list.html', ctx)
```
- 模板
```django
<section class="container">
<div class="content-wrap">
<div class="content">
  <div class="title">
	<h3 style="line-height: 1.3">博客列表</h3>
  </div>
  {% for post in post_list.object_list %}
  <article class="excerpt excerpt-1"><a class="focus" href="/blog/{{post.id}}" title="{{post.title}}" target="_blank" >
    <img class="thumb" data-original="/{{post.cover}}" src="/{{post.cover}}" alt="{{post.title}}"  style="display: inline;"></a>
	<header><a class="cat" href="/category/{{post.category.id}}" title="{{post.category.name}}" >{{post.category.name}}<i></i></a>
	  <h2><a href="/blog/{{post.id}}" title="{{post.title}}" target="_blank" >{{post.title}}</a></h2>
	</header>
	<p class="meta">
	  <time class="time"><i class="glyphicon glyphicon-time"></i> {{post.pub_date|date:'Y-m-d'}}</time>
	  <span class="views"><i class="glyphicon glyphicon-eye-open"></i> {{post.views}}</span>
    <a class="comment" href="##comment" title="评论" target="_blank" ><i class="glyphicon glyphicon-comment"></i>{{post.comment_set.count}}</a></p>
	<p class="note">{{post.content}}</p>
  </article>
  {% endfor %}

  {% include "_pagination.html" %}
```
- _pagination.html
```django
{% load i18n %}
<div class="pagination">
    {% if post_list.has_previous %}
        <a href="?{{ post_list.previous_page_number.querystring }}" class="prev">&lsaquo;&lsaquo; 上一页</a>
    {% else %}
        <span class="disabled prev">&lsaquo;&lsaquo; 上一页</span>
    {% endif %}
    {% for page in post_list.pages %}
        {% if page %}
            {% ifequal page post_list.number %}
                <span class="current page">{{ page }}</span>
            {% else %}
                <a href="?{{ page.querystring }}" class="page">{{ page }}</a>
            {% endifequal %}
        {% else %}
            ...
        {% endif %}
    {% endfor %}
    {% if post_list.has_next %}
        <a href="?{{ post_list.next_page_number.querystring }}" class="next">下一页 &rsaquo;&rsaquo;</a>
    {% else %}
        <span class="disabled next">下一页 &rsaquo;&rsaquo;</span>
    {% endif %}
</div>

```


# 十六、实现标签云功能
```django
def blog_list(request):
    post_list = Post.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(post_list, per_page=1, request=request)

    post_list = p.page(page)

    tags = Tags.objects.all()
    tag_message_list = []
    for t in tags:
        count = len(t.post_set.all())
        tm = TagMessage(t.id, t.name, count)
        tag_message_list.append(tm)

    ctx = {
        'post_list': post_list,
        'tags': tag_message_list
    }
    return render(request, 'list.html', ctx)
```
- 模板
```html
	<h3>标签云</h3>
	<div class="widget-sentence-content">
		<ul class="plinks ptags">

      {% for t in tags %}
			<li><a href="/tags/{{t.tid}}" title="{{t.name}}" draggable="false">{{t.name}} <span class="badge">{{t.count}}</span></a></li>
      {% endfor %}
		</ul>
	</div>
  </div>
```
# 十七、实现分类查询功能
- 编写视图
```django
def blog_list(request, cid=-1):
    post_list = None
    if cid != -1:
       cat = BlogCategory.objects.get(id=cid)
       post_list = cat.post_set.all()
    else:
       post_list = Post.objects.all()

    ....

    ctx = {
        'post_list': post_list,
        'tags': tag_message_list
    }
    return render(request, 'list.html', ctx)
```
- 编写路由
```django
url(r'^category/(?P<cid>[0-9]+)/$', blog_list),
```
- 模板 index
```html
  <div class="title">
	<h3>最新发布</h3>
	<div class="more">
      {%for c in blogcategory_list%}
			  <a href="/category/{{c.id}}" title="{{c.name}}" >{{c.name}}</a>
			{% endfor %}
		</div>
  </div>
```
# 十八、实现按标签查询功能
- 编写views
```django
def blog_list(request, cid=-1, tid=-1):
    post_list = None
    if cid != -1:
       cat = BlogCategory.objects.get(id=cid)
       post_list = cat.post_set.all()
    elif tid != -1:
       tag = Tags.objects.get(id=tid)
       post_list = tag.post_set.all()
    else:
       post_list = Post.objects.all()

    ....

    ctx = {
        'post_list': post_list,
        'tags': tag_message_list
    }
    return render(request, 'list.html', ctx)
```
- 路由设置
```django
url(r'^tags/(?P<tid>[0-9]+)/$', blog_list),
```
- 模板
```django
	<h3>标签云</h3>
	<div class="widget-sentence-content">
		<ul class="plinks ptags">

      {% for t in tags %}
			<li><a href="/tags/{{t.tid}}" title="{{t.name}}" draggable="false">{{t.name}} <span class="badge">{{t.count}}</span></a></li>
      {% endfor %}
		</ul>
	</div>
  </div>
</div>
```
# 十九、实现博客详情功能
- 定义视图函数
```python
def blog_detail(request,bid):
    post = Post.objects.get(id=bid)
    post.views = post.views + 1
    post.save()

   

    # 博客标签
    tag_list = post.tags.all()

   
    ctx = {
        'post': post,
        

    }
    return render(request, 'show.html', ctx)
```
- 路由设置
```python
url(r'^blog/(?P<bid>[0-9]+)/$', blog_detail, name='blog_detail'),
```

- 前端展示

```html
{% extends 'base.html' %}
{% block title %}知奇博客-详细 {% endblock %}

{% block content %}
<section class="container">
<div class="content-wrap">
<div class="content">
  <header class="article-header">
	<h1 class="article-title"><a href="#" title="{{post.title}}" >{{post.title}}</a></h1>
	<div class="article-meta"> <span class="item article-meta-time">
	  <time class="time" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="发表时间：{{post.pub_date|date:'Y-m-d'}}">
      <i class="glyphicon glyphicon-time"></i> {{post.pub_date|date:'Y-m-d'}}</time>
	  </span>
    <span class="item article-meta-source" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="来源：{{post.user.username}}">
      <i class="glyphicon glyphicon-globe"></i> {{post.user.username}}</span>
      <span class="item article-meta-category" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="{{post.category.name}}">
        <i class="glyphicon glyphicon-list"></i> <a href="#" title="{{post.category.name}}" >{{post.category.name}}</a></span>
        <span class="item article-meta-views" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="浏览量：{{post.views}}">
          <i class="glyphicon glyphicon-eye-open"></i> {{post.views}}</span>
          <span class="item article-meta-comment" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="评论量">
          <i class="glyphicon glyphicon-comment"></i> </span> </div>
  </header>
  <article class="article-content">

    <p>{{post.content}}</p>


  </article>
  <div class="article-tags">标签：
    {% for tag in post.tags.all %}
      <a href="/tags/{{tag.id}}">{{tag.name}}</a>
    {% endfor %}
	</div>
 
{% endblock %}
```

# 二十、实现相关推荐功能
# 二十一、实现发表评论的功能
# 二十二、实现评论列表功能
# 二十三、实现登录功能
# 二十四、实现注册功能
# 二十五、实现注册验证功能
# 二十六、实现注销功能
# 二十七、实现后台富文本功能