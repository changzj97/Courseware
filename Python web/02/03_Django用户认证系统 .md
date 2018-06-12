---
title: Django用户认证系统
tags: Django
notebook: 7.0第五月 Python_web后端
---


[toc]

# 用户身份验证
## 设置身份验证
在使用 Django 提供的身份验证机制之前,要在项目的 settings.py 文件中添加相关的设置。
在 settings.py 文件中找到 INSTALLED_APPS 列表,检查有没有列出 django.contrib.auth 和 django.contrib.contenttypes 。 INSTALLED_APPS 列表应该类似下面这样:
```python
INSTALLED_APPS =[
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'rango',
]
```
``django.contrib.auth`` 用于访问 Django 提供的身份验证系统,而 ``django.contrib.contenttypes`` 供auth 应用跟踪数据库中的模型。

> 如果 INSTALLED_APPS 列表中没有 django.contrib.auth 和 django.contrib.contenttypes ,要自己添加,添加后还要执行 python manage.py migrate 命令更新数据库,添加所需的表,例如 User 模型的表。
在 Django 项目中添加新的应用后,一般最好执行 migrate 命令,以防应用中有模型要与底层数据库同步。
## 密码哈希
任何情况下都不能在数据库中存储明文密码。 1 如果包含用户账户的数据库落到不怀好意的人手上,可能造成天大的灾难。幸好,Django 的 auth 应用默认存储的是经过 PBKDF2 算法计算过的密码哈希值,可以有效保护用户数据的安全。然而,如果你想进一步控制生成密码哈希值的方式,可以在项目的 settings.py 模块中更换 Django 使用的算法。为此,添加PASSWORD_HASHERS 元组,例如:

```python
PASSWORD_HASHERS = (
'django.contrib.auth.hashers.PBKDF2PasswordHasher',
'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
)
```
罗列哈希算法的顺序很重要,Django 将使用 PASSWORD_HASHERS 中的第一个哈希算法( settings.PASSWORD_HASHERS[0] )。如果第一个无效,而且还有其他哈希算法供选择,Django将依次尝试后面的算法。
如果想使用更为安全的哈希算法,可以安装 Bcrypt( pip install bcrypt ),然后把PASSWORD_HASHERS 设为:
```python
PASSWORD_HASHERS = [
'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
'django.contrib.auth.hashers.BCryptPasswordHasher',
'django.contrib.auth.hashers.PBKDF2PasswordHasher',
'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]
```
## 密码验证器
鉴于人们经常使用相对容易猜出的密码,Django 1.9 引入了一个备受期待的新功能——密码验证。在 Django 项目的 settings.py 模块中有个字典构成的列表,名为 AUTH_PASSWORD_VALIDATORS 。在嵌套的字典中可以清楚地看出,Django 1.9 自带了一些常用的密码验证器,例如针对长度的验
证器。每个验证器都有 OPTIONS 字典,以便自定义选项。假如你想确保密码最短为 6 个字符,那么可以把 MinimumLengthValidator 的 min_length 选项设为 6 ,如下所示:
```python
AUTH_PASSWORD_VALIDATORS = [
...
{
'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
'OPTIONS': { 'min_length': 6, }
},
...
]
```
除了自带的密码验证器之外,还可以自定义。本书不介绍具体方法,如果感兴趣,请阅读 Django文档。
## User模型
User 对象( django.contrib.auth.models.User )是 Django 身份验证系统的核心,表示与 Django应用交互的每个个体。根据 Django 文档,身份验证系统的很多方面都能用到 User 对象,例如访问限制、注册新用户,以及网站内容与创建者之间的关系。

User 模型有 5 个主要属性:
- 用户账户的用户名( username )
- 用户账户的密码( password )
- 用户的电子邮件地址( email )
- 用户的名字( first_name )
- 用户的姓( last_name )

此外, User 模型还有其他属性,例如 is_active 、 is_staff 和 is_superuser 。这些属性的值都是布尔值,分别用于指明账户是否激活、是否为团队成员,以及是否拥有超级用户权限。 User 模型的完整属性列表参阅 Django 文档。
## 增加用户属性
除了 User 模型提供的属性之外,如果还需要其他用户相关的属性,要自己定义一个与 User 模型关联的模型。对 Rango 应用而言,我们想为用户账户增加两个属性:
- 一个 URLField ,让 Rango 的用户设定自己的网站
- 一个 ImageField ,让 Rango 的用户设定自己的头像

为此,要在 Rango 应用的 models.py 文件中定义一个模型。我们把这个模型命名为 UserProfile 。

```python
class UserProfile(models.Model):
    # 这一行是必须的
    # 建立与 User 模型之间的关系
    user = models.OneToOneField(User)
    # 想增加的属性
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # 覆盖 __str__() 方法,返回有意义的字符串
    # 如果使用 Python 2.7.x,还要定义 __unicode__ 方法
    def __str__(self):
        return self.user.username
```
> 注意,这个模型与 User 模型之间建立的一对一关系。因为引用了默认的 User 模型,所以要在models.py 文件中导入它:
```python
from django.contrib.auth.models import User
```
我们为 Rango 应用的用户账户增加了两个字段,还提供了 ``__str__()`` 方法,以便在需要UserProfile 实例的字符串表示形式时返回有意义的值。注意,使用 Python 2 的话,还要定义``__unicode__()`` 方法,返回用户名的 Unicode 格式。

我们增加的 website 和 picture 字段都设定了 blank=True 。因此这两个字段都可以为空,不是必须要提供值。

此外,注意 ImageField 字段的 upload_to 参数。


如果想通过 Django 管理界面访问 UserProfile 模型数据,在 Rango 应用的 admin.py 模块中导入
UserProfile 模型:
```python
from rango.models import UserProfile
```
然后注册模型:
```python
admin.site.register(UserProfile)
```

## 创建用户注册视图和模板

一切准备妥当之后,接下来实现用户注册功能。为此,我们要定义一个新视图、创建一个模板,并添加一个 URL 映射。

> 注意,有一些现成的用户注册应用可以拿来直接使用,无需我们自己动手实现注册和登录功能。
然而,在使用这样的应用之前最好了解一下底层机制。没有痛苦就没有收获。在这个过程中还能巩固你对表单的理解,学会如何扩展 User 模型,以及如何上传媒体文件。

实现用户注册功能的步骤如下:

- 定义 UserForm 和 UserProfileForm
- 添加一个视图,处理创建新用户的过程
- 创建一个模板,显示 UserForm 和 UserProfileForm
- 把 URL 映射到前面添加的视图上

最后,还要在首页添加一个链接,指向注册页面。

### 定义 UserForm 和 UserProfileForm

我们要在 rango/forms.py 中定义两个类,继承自 forms.ModelForm 。其中一个针对 User 类,另一个针对前面定义的 UserProfile 模型。这两个 ModelForm 子类创建的 HTML 表单用于显示相应模型的字段,为我们节省了很多工作量。
首先,在 rango/forms.py 文件中定义两个继承自 forms.ModelForm 的类。

```python
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
```

注意,这两个类中都有 Meta 类。如其名所示, Meta 类的作用是为所在的类提供额外的属性。 Meta类中必须有 model 字段。 UserForm 类对应的模型是 User 。此外,还要通过 fields 或 exclude 指定要在表单中显示或排除的字段。

这里,我们只想显示 User 模型的 username 、 email 和 password 字段,以及 UserProfile 模型的website 和 picture 字段。 UserProfile 模型的 user 字段在注册用户时设定。这是因为创建UserProfile 实例时,还没有 User 实例可用。

此外,注意 UserForm 中定义了 password 属性。虽然 User 模型实例有 password 属性,但是在渲染的 HTML 表单中这个字段的值不会被遮盖,用户输入的密码是可见的。鉴于此,我们重新定义了password 属性,指定使用 PasswordInput() 小组件显示这个 CharField ,以防用户输入的密码被人窥见。

最后,别忘了在 forms.py 模块的顶部导入所需的类。为了便于你参考,下面给出导入语句:
```python
from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile
```
### 定义 register() 视图
接下来要渲染表单及处理表单数据。在 Rango 应用的 views.py 模块中,添加一个 import 语句,导入新定义的 UserForm 和 UserProfileForm 类。
```python
from rango.forms import UserForm, UserProfileForm
```
然后定义 register() 视图:
```python
def register(request):
    # 一个布尔值,告诉模板注册是否成功
    # 一开始设为 False,注册成功后改为 True
    registered = False
    # 如果是 HTTP POST 请求,处理表单数据
    if request.method == 'POST':
        # 尝试获取原始表单数据
        # 注意,UserForm 和 UserProfileForm 中的数据都需要
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # 如果两个表单中的数据是有效的......
        if user_form.is_valid() and profile_form.is_valid():
            # 把 UserForm 中的数据存入数据库
            user = user_form.save()
            # 使用 set_password 方法计算密码哈希值
            # 然后更新 user 对象
            user.set_password(user.password)
            user.save()
            # 现在处理 UserProfile 实例
            # 因为要自行处理 user 属性,所以设定 commit=False
            # 延迟保存模型,以防出现完整性问题
            profile = profile_form.save(commit=False)
            profile.user = user
            # 用户提供头像了吗?
            # 如果提供了,从表单数据库中提取出来,赋给 UserProfile 模型
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                # 保存 UserProfile 模型实例
                profile.save()
                # 更新变量的值,告诉模板成功注册了
                registered = True
            else:
                # 表单数据无效,出错了?
                # 在终端打印问题
                print(user_form.errors, profile_form.errors)
        else:
            # 不是 HTTP POST 请求,渲染两个 ModelForm 实例
            # 表单为空,待用户填写
            user_form = UserForm()
            profile_form = UserProfileForm()
            # 根据上下文渲染模板
        return render(request,'rango/register.html',{'user_form': user_form,'profile_form': profile_form,'registered': registered})
```
这个视图看似复杂,其实与添加分类和添加网页的视图十分相似。这里,我们要处理两个不同的ModelForm 实例,一个针对 User 模型,一个针对 UserProfile 模型。如果用户上传了头像,还要处理头像图片。
此外,还要建立两个模型实例之间的关系。为此,我们先创建 User 模型实例,然后在UserProfile 实例中引用它: profile.user = user 。 UserProfileForm 表单的 user 属性必须这样设定,不能让用户自行填写。
### 创建注册页面模板
现在要创建 register() 视图的模板。新建 rango/register.html 文件,写入下述代码。

```html
{% extends 'rango/base.html' %}
{% load staticfiles %}
{% block title_block %}
    Register
{% endblock %}
{% block body_block %}
<h1>Register for Rango</h1>
{% if registered %}
    Rango says: <strong>thank you for registering!</strong>
    <a href="{% url 'index' %}">Return to the homepage.</a><br/>
    {%
{% else %}
    Rango says: <strong>register here!</strong><br/>
    <form id="user_form" method="post" action="{% url 'register' %}"
          enctype="multipart/form-data">
        {% csrf_token %}
        <!-- 显示每个表单
        -->
        {{ user_form.as_p }}
        {{ profile_form.as_p }}
        <!-- 提供一个按钮,点击后提交表单 -->
        <input type="submit" name="submit" value="Register"/>
    </form>
{% endif %}
endblock %}
```
注意,这个模板使用视图中的 registered 变量判断注册是否成功。 registered 的值为 False 时,显示注册表单;否则,显示成功注册消息。
此外,我们在 user_form 和 profile_form 上调用了 as_p 模板函数。这么做的目的是在段落(HTML ``<p>`` 标签)中显示各个表单元素,一行显示一个表单元素。

最后注意,我们为 ``<form>`` 元素设定了 enctype 属性。这是因为,如果用户想上传头像,表单数据中将包含二进制数据,而且可能相当大。传给服务器时,这些数据要分成几部分。因此,我们要设定 enctype="multipart/form-data" ,让 HTTP 客户端(Web 浏览器)分段打包和发送数据。如若不然,服务器收不到用户提交的全部数据。

此外,别忘了在表单中添加 CSRF 令牌,即 {% csrf_token %} 。否则,Django 的跨站请求伪造保护中间件将拒绝接收表单的内容,返回错误。

### 添加 URL 映射
有了视图和对应的模板之后,现在可以添加 URL 映射了。打开 Rango 应用的 urls.py 模块,根据下述代码修改 urlpatterns 。
```python
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category,
        name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        views.add_page,
        name='add_page'),
    url(r'^register/$',
        views.register,
        name='register'),  # 新增的模式
]

```
新增的模式把 /rango/register/ URL 映射到 register() 视图上。注意,我们为这个新模式设定了name 参数,以便在模板中使用 url 引用,例如 {% url 'register' %} 。

### 添加链接
最后,在 base.html 模板中添加一个链接,指向注册页面。参照下述代码更新无序列表中的链接,在 Rango 应用的每个页面中都添加指向注册页面的链接。
![选区_013](https://i.loli.net/2018/06/11/5b1e97ab1741b.png)

### 检验结果
一切就绪之后,该检验结果了。启动 Django 开发服务器,注册一个用户试试。如果愿意,上传一个头像。注册表单如图所示。
![1](https://i.loli.net/2018/06/11/5b1e97f739f36.png)
看到成功注册消息后, User 和 UserProfile 模型在数据库中应该都会增加一条记录。在 Django 管理界面中确认是不是这样。

# 实现登录功能

用户能注册账户之后,接下来要让用户能够登录。为此,要执行以下几步:
- 定义一个视图,处理登录凭据
- 创建一个模板,显示登录表单
- 在首页添加登录链接

## 定义登录视图
```python
def user_login(request):
    # 如果是 HTTP POST 请求,尝试提取相关信息
    if request.method == 'POST':
        # 获取用户在登录表单中输入的用户名和密码
        # 我们使用的是 request.POST.get('<variable>')
        # 而不是 request.POST['<variable>']
        # 这是因为对应的值不存在时,前者返回 None,
        # 而后者抛出 KeyError 异常
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 使用 Django 提供的函数检查 username/password 是否有效
        # 如果有效,返回一个 User 对象
        user = authenticate(username=username, password=password)
        # 如果得到了 User 对象,说明用户输入的凭据是对的
        # 如果是 None(Python 表示没有值的方式),说明没找到与凭据匹配的用户
    if user:
        # 账户激活了吗?可能被禁了
        if user.is_active:
            # 登入有效且已激活的账户
            # 然后重定向到首页
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            # 账户未激活,禁止登录
            return HttpResponse("Your Rango account is disabled.")
    else:
        # 提供的登录凭据有问题,不能登录
        print("Invalid login details: {0}, {1}".format(username, password))
        return HttpResponse("Invalid login details supplied.")
    # 不是 HTTP POST 请求,显示登录表单
    # 极有可能是 HTTP GET 请求
    else:
        # 没什么上下文变量要传给模板系统
        # 因此传入一个空字典
        return render(request, 'rango/login.html', {})
```
跟之前一样,因为要处理不同的情况,这个视图看起来十分复杂。从上述代码可以看出,user_login() 视图既能渲染登录表单(包含 username 和 password 两个字段),也能处理表单数据。

如果通过 HTTP GET 方法访问这个视图,显示登录表单。然而,如果通过 HTTP POST 请求访问,则处理表单数据。

如果通过 POST 请求发送有效的表单数据,从中提取用户名和密码。然后使用 Django 提供的authenticate() 函数检查用户名和密码是否匹配某个用户账户。如果能找到这样的用户,返回一个 User 对象,否则返回 None 。

返回 User 对象时,检查账户是否激活。如果是激活的,调用 Django 提供的 login() 函数,登入用户。

然而,如果发送的表达数据无效,例如用户名和密码没有都填,登录表单显示错误消息,提示用户名或密码无效。

你可能注意到了,这里用了一个新类,即 HttpResponseRedirect 。从名称可以看出,HttpResponseRedirect 实例生成的响应让 Web 浏览器重定向到参数指定的 URL。注意,响应的HTTP 状态码是表示重定向的 302,而不是表示成功的 200。详情参见 Django 文档。

最后,使用 Django 提供的 reverse() 函数获取 Rango 应用首页的 URL。 reverse() 函数在 Rango应用的 urls.py 模块中查找名为 index 的 URL 模式,解析出对应的 URL。如果以后修改了 URL 映射,视图代码不受影响。

user_login() 视图用到了 Django 提供的多个函数和类,因此要导入它们。下述 import 语句必须放在 rango/views.py 文件的顶部。


```python
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
```

有了视图之后,我们还要创建一个模板,让用户输入登录凭据。现在你应该知道要把模板放在templates/rango/ 目录中,不过这个模板的名称我不告诉你,请你根据 user_login() 视图的代码确定。在模板中写入下述代码:
```html
{% extends 'rango/base.html' %}
{% load staticfiles %}
{% block title_block %}
Login
{% endblock %}
{% block body_block %}
<h1>Login to Rango</h1>
<form id="login_form" method="post" action="{% url 'login' %}">
{% csrf_token %}
Username: <input type="text" name="username" value="" size="50" />
<br />
Password: <input type="password" name="password" value="" size="50" />
<br />
<input type="submit" value="submit" />
</form>
{% endblock %}
```
input 元素的 name 属性要与 user_login() 视图中的保持一致。也就是说,用户名输入框的 name属性的值应该是 username ,而密码输入框的 name 属性的值应该是 password 。此外,别忘了 {%csrf_token %} 。

## 添加URL映射

创建好登录模板之后,接下来要把 user_login() 视图映射到一个 URL 上。修改 Rango 应用的urls.py 模块,在 urlpatterns 列表中添加下述映射:
```python
url(r'^login/$', views.user_login, name='login'),
```
## 添加链接
最后,添加一个链接,方便 Rango 的用户访问登录页面。编辑 templates/rango/ 目录中的 base.html模板,在无序列表中添加下述链接:
```html
<ul>
...
<li><a href="{% url 'login' %}">Login</a><li>
</ul>
```
如果愿意,还可以修改首页的页头,向已登录的用户显示独特的欢迎消息,而未登录的用户则显示一般的欢迎消息。在 index.html 模板中找到现在的欢迎消息:``hey there partner``
把这一行改成:
```html
{% if user.is_authenticated %}
howdy {{ user.username }}!
{% else %}
hey there partner!
{% endif %}
```
可以看出,我们使用 {% if user.is_authenticated %} 检查用户是否通过身份验证。如果用户已登录,我们能访问 user 对象。因此,我们可以通过这个对象判断用户是否登录(验证身份)。如果用户已登录,我们便能获取关于用户的更多信息。在这个示例中,当用户登录后,我们获取用户的用户名。如果用户未登录,则显示一般的欢迎消息,即“hey there partner!”。

## 检验结果
启动 Django 开发服务器,尝试登录

![2](https://i.loli.net/2018/06/12/5b1f54bb36fb0.png)

至此,用户登录功能可用了。请启动 Django 开发服务器,注册一个新账户试试。成功注册后,你应该能使用自己设定的凭据登录。