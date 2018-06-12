---
title: Django ORM(关系) 和 分页
tags: Django
notebook: 7.0第五月 Python_web后端
---

[toc]

# 一对一关系：（OneToOneField)
应用场景举例：通常我们定义一个用户表User会将常用的字段如（name, email ,phone)放在一张表中，不常用的字段（address)如用户地址放在另张表中UserInfo。这样做的优势是数据库层面上表中的字段更少，读写速度更快。
举个栗子:
```python
from django.db import models
class User(models.Model):
   name = models.CharField(max_length=200,null=False)
   phone = models.CharField(max_length=200,null=False)
   email = models.CharField(max_length=200,null=False)
   
class UserInfo(models.Model):
    address = models.CharField(max_length=200）
    user = models.OneToOneField('User')  
#  定义一个一对一关系使用models.OneToOneField('')
#  数据库中相当于建立了一个unique外键关联(user_id) 
```
命令行执行
```python
1.python manage.py makemigrations 
2.python manage.py migrate
```
将数据表添加到数据库中：

添加数据表后可以查看UserInfo数据表中也会有一个user_id字段并且unique=True.这是Django一对一关系的数据库层的处理方式：
user_info DDL是：
```sql
CREATE TABLE `orm_demo_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(200) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `orm_demo_userinfo_user_id_be94d8f9_fk_orm_demo_user_id` FOREIGN KEY (`user_id`) REFERENCES `orm_demo_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
```
一对一关系的数据添加/查询
```python
 def index(request):
    user = User(name='张三', email='1397350942@qq.com')
    user.save()  # 保存用户信息
    userinfo = UserInfo(address='CMU')
    userinfo.user = user 
    userinfo.save()
    # 查询
    user = User.objects.get(pk=1)
    userinfo = user.userinfo 
    return HttpResponse('opreation success')
```

# 一对多关系:
应用场景举例：如果我们需要给Article表一篇文章添加评论，通常一篇文章的评论会有多条

因此在Comments表中设置一个外键(models.ForeignKey)关联Article
举个栗子:
```python
class Article(models.Model):
    article_name = models.CharField(max_length=200,null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey('User',on_delete=models.CASCADE)   # models.CASECODE级联删除
    # 如果需要引用别的APP下的model 引用模型为 app_name.model_name author = models.ForeignKey('DTL_demo.User',on_delete=models.CASCADE)

    def __str__(self):
        return '<Article %r>' % self.article_name

class Comment(models.Model):
    comment = models.CharField(max_length=200,null=False)
    user = models.ForeignKey('User',on_delete=models.CASCADE)   
    article = models.ForeignKey('Article',on_delete=models.CASCADE)
```
设置外键关联的方式是设置一个字段

feilds=models.ForeignKey('关联的表的模型'，on_delete='',related_name=None)

on_delete：设置Django层面的外键约束方式有以下几种模式：

 - CASCADE 级联删除 如果引用的外键在主表中被删除，关联的数据也删除
 - PROTECT 受保护的模式，如果有其他表引用了要删除表的数据，那么该条数据不能进行删 除操作
 - SET 设置值
 - SET_NULL 设为空值
 - SET_DEFAULT 设置默认值
 - DO_NOTHING 不做任何操作，外键约束按照数据库的设置去处理
 
 
related_name: 可以设置引用的名字，默认为模型名字的小写（comment)


# 多对多关系：(ManyToManyField)

应用场景举例:

通常Article表中一篇文章会有多个标签，Tags表中的一个标签也会对应多篇文章
```python
class Article(models.Model):
    article_name = models.CharField(max_length=200,null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey('User',on_delete=models.CASCADE)   # models.CASECODE级联删除
    # 如果需要引用别的APP下的model 引用模型为 app_name.model_name author = models.ForeignKey('DTL_demo.User',on_delete=models.CASCADE)

    def __str__(self):
        return '<Article %r>' % self.article_name

class Tags(models.Model):
    # 多对多的关系 通过models.ManytoManyField('
    name = models.CharField(max_length=200, null=False)
    article = models.ManyToManyField('Article',related_name='tags')
```
多对多关系定义是用models.ManyToMany

映射到数据库中Django会在数据库中建立一个中间表，中间表中存放了文章id 和标签id