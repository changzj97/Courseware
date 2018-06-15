---
title: 乐农电商(Dajngo版)
tags: Django
notebook: 7.0第五月 Python_web后端
---


[toc]


# 创建项目
## 创建项目&创建应用
- 项目名称: 乐农优选
- project_name: Leong preferred
## 配置数据库
```python
# 只是一个代码示例,取自官方文档
# https://docs.djangoproject.com/en/1.8/ref/settings/
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
## 静态资源管理
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```
## 导入模板
- 拷贝相关静态资源文件到static目录
链接：https://pan.baidu.com/s/11IApw1Vnq9pgvukjLdrHBg 密码：g37y

- 拷贝HTML文件到模板templates目录 

## 分析字段、设计模型类
- 创建模型类
```python
# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)  # 姓名
    upwd = models.CharField(max_length=40)  # 密码
    uemail = models.CharField(max_length=30)  # 邮箱
    ureceive = models.CharField(max_length=20)  # 收件人
    uaddress = models.CharField(max_length=100)  # 地址
    uzip_code = models.CharField(max_length=6)  # 邮编
    uphone = models.CharField(max_length=11)  # 手机
```
- 生成迁移、执行迁移文件
```python
python manage.py makemigrations 
python manage.py migrate 
```
> python3需要注意在项目``__init__``下面:
```python
import pymysql
pymysql.install_as_MySQLdb()
```
# 注册
## 定义视图
```python
def register(request):
    return render(request,'register.html')
```
## 配置URL
```python
from LeongApp import urls as Leong_user_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include(Leong_user_urls))
]
```

```python
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
]

```
## 页面显示错误排查
![Alt text](./1525963023520.png)

``遇到此类问题从这几个地方去考虑：``

- settings.py是否配置静态文件路径
- static目录是否导入静态文件
- HTML模板里面的路径对不对
 ![Alt text](./1525963488387.png)

## 配置页面
- 创建一个base页面
```htmlbars
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<title>乐农优选-{{ title }}</title>
	<link rel="stylesheet" type="text/css" href="/static/css/reset.css">
	<link rel="stylesheet" type="text/css" href="/static/css/main.css">
	<script type="text/javascript" src="/static/js/jquery-1.12.4.min.js"></script>
	{% block head %}{% endblock %}
</head>
<body>
{% block body %}{% endblock %}
{% block footer %}{% endblock %}
</body>
</html>
```
- 集成base页面
```htmlbars
{% extends 'base_foot.html' %}
{% block head %}
    <script type="text/javascript" src="/static/js/register.js"></script>{% endblock %}

{% block body %}
    <div class="register_con">
        <div class="l_con fl">
            <a class="reg_logo"><img src="/static/images/logo02.png"></a>
            <div class="reg_slogan">足不出户 · 新鲜每一天</div>
            <div class="reg_banner"></div>
        </div>

        <div class="r_con fr">
            <div class="reg_title clearfix">
                <h1>用户注册</h1>
                <a href="#">登录</a>
            </div>
            <div class="reg_form clearfix">
                <form>
                    <ul>
                        <li>
                            <label>用户名:</label>
                            <input type="text" name="user_name" id="user_name">
                            <span class="error_tip">提示信息</span>
                        </li>
                        <li>
                            <label>密码:</label>
                            <input type="password" name="pwd" id="pwd">
                            <span class="error_tip">提示信息</span>
                        </li>
                        <li>
                            <label>确认密码:</label>
                            <input type="password" name="cpwd" id="cpwd">
                            <span class="error_tip">提示信息</span>
                        </li>
                        <li>
                            <label>邮箱:</label>
                            <input type="text" name="email" id="email">
                            <span class="error_tip">提示信息</span>
                        </li>
                        <li class="agreement">
                            <input type="checkbox" name="allow" id="allow" checked="checked">
                            <label>同意”乐农优选用户使用协议“</label>
                            <span class="error_tip2">提示信息</span>
                        </li>
                        <li class="reg_sub">
                            <input type="submit" value="注 册" name="">
                        </li>
                    </ul>
                </form>
            </div>

        </div>

    </div>
{% endblock %}
{% block footer %}
    <div class="footer no-mp">
        <div class="foot_link">
            <a href="#">关于我们</a>
            <span>|</span>
            <a href="#">联系我们</a>
            <span>|</span>
            <a href="#">招聘人才</a>
            <span>|</span>
            <a href="#">友情链接</a>
        </div>
        <p>CopyRight © 2016 乐农优选信息技术有限公司 All Rights Reserved</p>
        <p>电话：010-****888 京ICP备*******8号</p>
    </div>
{% endblock %}

```

## 表单提交
- 模板表单相关配置
![Alt text](./1525965456492.png)


```django
<form action="/user/register_handle/" method="post">
                    {% csrf_token %}
```
>  {% csrf_token %}  防止跨站攻击 

- 定义 register_handle 视图接受表单内容
- 接收用户输入
- 判断两次密码，如果两次密码不一致，可以直接重定向返回注册页
- 创建模型类对象,用户存储数据
- 修改模型类,否则无法存储数据
- 注册成功返回登录页面

**模型类**
```python
# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)  # 姓名
    upwd = models.CharField(max_length=40)  # 密码
    uemail = models.CharField(max_length=30)  # 邮箱
    ureceive = models.CharField(max_length=20, default='')  # 收件人
    uaddress = models.CharField(max_length=100, default='')  # 地址
    uzip_code = models.CharField(max_length=6, default='')  # 邮编
    uphone = models.CharField(max_length=11, default='')  # 手机
    # default,blank是Python层面的约束,不影响数据库表结构
```
**视图类**
```python
def register_handle(request):
    # 接收用户输入
    uname = request.POST.get('user_name', '无')
    upwd = request.POST.get('pwd', '无')
    upwd2 = request.POST.get('cpwd', '无')
    uemail = request.POST.get('email', '无')
    # 判断两次密码
    if upwd != upwd2:
        # 如果没有密码不一致 我们就直接重定向返回注册页
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode('utf8'))
    upwd3 = s1.hexdigest()

    # 创建模型类对象
    user = models.UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    # 注册成功,跳转到登录页面
    return redirect('/user/login/')
```

# 模型设计

## 创建商品应用
- 应用名称：leong_goods
## 模型类设计

- 设计首页商品分类的模型
```python
class TypeInfo(models.Model):
    """商品分类"""
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    """商品"""
    gtitle = models.CharField(max_length=20)
    # 图片位置
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    # 单位
    gunit = models.CharField(max_length=20, default='500g')
    # 点击量  用于排序
    gclick = models.IntegerField()
    # 简介
    gjianjie = models.CharField(max_length=200)
    # 库存
    gkucun = models.IntegerField()
    # 详细介绍
    gcontent = HTMLField()
    #
    gtype = models.ForeignKey(TypeInfo)

    def __str__(self):
        return self.gtitle.encode('utf-8')
```
- 配置开发阶段,我们图片上传的目录路径
```python
# 开发阶段上传文件目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
```
## 作业
1. 修复用户名一致仍然可以注册的BUG
2. 修复邮箱一致仍旧可以注册的BUG
# 首页
# 列表页
# 详情页
# 登录验证
# 退出
# 最近浏览
# 设计模型
# 购买商品
# 全选全消
# 修改、删除
# 订单
# 全文检索
# 自定义上下文
