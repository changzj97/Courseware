---
title: Flask web框架
tags: 
notebook: 7.0第五月 Python_web后端
---

[toc]

# 基础教程
## 第一个Flask应用
- 安装flask
```python
pip install flask
```
- 第一个flask应用
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```
- 运行应用
## 路由规则
## 通过视图函数获得URL
## 模板渲染和静态文件
## HTTP方法
## 访问request请求
## 文件上传
## cookie
## 请求重定向和错误处理
## session

# Flask_SQLALchemy
## Flask_SQLALchemy 简介
## Flask_SQLALchemy 模型
## Flask_SQLALchemy CRUD
## Flask_SQLALchemy 综合应用

# Flask_WTF
## 创建表单和验证表单
## Flask_WTF 表单字段
## Flask_WTF 表单样式

# Flask留言板
## 项目演示
## 创建模型
## 配置模板和路由
## 创建表单
## 添加和显示留言
## 修改和删除留言