from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Banner, Post, BlogCategory, FriendlyLink, Comment, Tags
from django.db.models import Q


class Return_data():

    def return_comment(self):
        comment_list = Comment.objects.order_by('-pub_date')
        new_comment_list = []
        # 去重
        for t in comment_list:
            if t.post not in new_comment_list:
                new_comment_list.append(t.post)
        return new_comment_list

    def return_tags(self):
        tags_list = Tags.objects.all()
        return tags_list


r_data = Return_data()


def search(request):
    kw = request.POST.get('keyword')

    post_list = Post.objects.filter(Q(title__contains=kw) | Q(content__contains=kw))

    ctx2 = {
        'post_list': post_list,
        'comment_list': r_data.return_comment(),
        'tags_list': r_data.return_tags()
    }
    return render(request, 'list.html', ctx2)


# 这是博客的列表的视图函数
class Bloglist(View):
    def get(self, request, tid=-1):

        if tid != -1:
            post_list = Post.objects.filter(tags=tid)
        else:
            post_list = Post.objects.order_by('-pub_date')

        # 最新评论
        comment_list = Comment.objects.order_by('-pub_date')
        new_comment_list = []
        # 去重
        for t in comment_list:
            if t.post not in new_comment_list:
                new_comment_list.append(t.post)

        # 取出所有的标签
        tags_list = Tags.objects.all()

        ctx = {

            'post_list': post_list,
            'comment_list': new_comment_list,
            'tags_list': tags_list
        }

        return render(request, 'list.html', ctx)


# Create your views here.
# def index(request):
#     return render(request, 'index.html')

class Index(View):
    def get(self, request):
        # 轮播图的数据源
        banner_list = Banner.objects.all()
        # 推荐文章的数据源
        recomment_list = Post.objects.filter(recommend=True)
        # 博客分类
        category_list = BlogCategory.objects.all()
        # 取出所有的博客 按照时间倒序输出
        post_list = Post.objects.order_by('-pub_date')
        # 取出友情链接
        friendly_link = FriendlyLink.objects.all()
        # 最新评论
        comment_list = Comment.objects.order_by('-pub_date')
        new_comment_list = []
        # 去重
        for t in comment_list:
            if t.post not in new_comment_list:
                new_comment_list.append(t.post)

        ctx = {
            'banner_list': banner_list,
            'recomment_list': recomment_list,
            'category_list': category_list,
            'post_list': post_list,
            'friendly_link': friendly_link,
            'comment_list': new_comment_list
        }

        return render(request, 'index.html', ctx)

    # def post(self, request):
    #     pass


def blog_detail(request, pid):
    post_detail = Post.objects.get(id=pid)
    post_detail.views = post_detail.views+1
    post_detail.save()

    blog_count = Post.objects.all().count()

    # 相关推荐
    recoment_list = Post.objects.filter(category=post_detail.category)
    recoment_list_new = []
    for recoment in recoment_list:
        if recoment.id != post_detail.id:
            recoment_list_new.append(recoment)
    recoment_list = recoment_list_new

    ctx = {
        'post_detail': post_detail,
        'comment_list': r_data.return_comment(),
        'recoment_list': recoment_list,
        'blog_count':blog_count
    }
    return render(request, 'show.html', ctx)
