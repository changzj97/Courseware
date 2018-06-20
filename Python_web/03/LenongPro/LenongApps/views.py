from django.shortcuts import render
from .models import TypeInfo, Banner, GoodsInfo
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View


class Search_handle(View):
    def post(self, request):
        pass

    def get(self, request):
        keyword = request.GET.get('keywords')
        # 商品
        goods_list = GoodsInfo.objects.filter(gtitle__contains=keyword)
        # goods_type = goods_list[0].gtype
        # print(type(goods_type))
        # 空列表
        news_goods_list = []
        news_goods_list2 = []
        # 遍历 所有搜索到的商品
        for goods in goods_list:
            news_goods_list.extend(GoodsInfo.objects.filter(gtype=goods.gtype))
            if len(news_goods_list2) <= 2:
                for good in news_goods_list:
                    if good != goods:
                        news_goods_list2.append(goods)
        # news_goods_list2 = set(news_goods_list)

        ctx = {
            'goods_list': goods_list,
            # 'news_goods_type': news_goods_list2[:2]
        }
        return render(request, 'list.html', ctx)


def detail(request, gid=1):
    goods = GoodsInfo.objects.get(id=gid)

    news_goods_list = GoodsInfo.objects.filter(gtype=goods.gtype).filter(~Q(id=gid)).order_by('-gpub_date')[:2]
    news_goods_list_two = []
    # 排除自己本身
    for news_goods in news_goods_list:
        # if news_goods.id == gid:
        #     pass
        # else:
        #     news_goods_list_two.append(news_goods)
        if news_goods.id != goods.id:
            news_goods_list_two.append(news_goods)

    return render(request, 'detail.html', {'goods': goods, 'news_goods_list': news_goods_list_two})


def index(request):
    # 轮播图
    banner_list = Banner.objects.all()

    # 水果
    fruit_list = GoodsInfo.objects.filter(gtype__ttitle='新鲜水果')[:4]
    seafoods_list = GoodsInfo.objects.filter(gtype__ttitle='海鲜水产')[:4]
    meat_list = GoodsInfo.objects.filter(gtype__ttitle='猪牛羊肉')[:4]
    egg_list = GoodsInfo.objects.filter(gtype__ttitle='禽类蛋蛋')[:4]
    cai_list = GoodsInfo.objects.filter(gtype__ttitle='新鲜菜菜')[:4]
    sudo_list = GoodsInfo.objects.filter(gtype__ttitle='速冻品品')[:4]
    ctx = {
        'banner_list': banner_list,
        'fruit_list': fruit_list,
        'seafoods_list': seafoods_list,
        'meat_list': meat_list,
        'egg_list': egg_list,
        'cai_list': cai_list,
        'sudo_list': sudo_list
    }

    return render(request, 'index.html', ctx)


def goods_list(request, tid=-1):
    # 列表页

    if tid != -1:
        # 具体分类的列表页面
        goods_list = GoodsInfo.objects.filter(gtype__id=tid)
    else:
        # 全部
        goods_list = GoodsInfo.objects.all()

    # 新品推荐
    news_goods = TypeInfo.objects.get(id=tid)

    ctx = {
        'goods_list': goods_list,
        'news_goods_type': news_goods
    }

    return render(request, 'list.html', ctx)


def ajax_test(request):
    return render(request, 'ajax_text.html')


def ajax_handle(request):
    return JsonResponse({'key1': '1234'})
    # return HttpResponse('哈哈哈')
    # return render(request,'index.html')


def addshow(request):
    return render(request, 'ajax_add.html')


@csrf_exempt
def add_handele(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    c = int(a) + int(b)

    ctx = {
        'c': c
    }

    return JsonResponse(ctx)
