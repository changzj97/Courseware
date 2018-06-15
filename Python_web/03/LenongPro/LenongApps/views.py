from django.shortcuts import render
from .models import TypeInfo


# Create your views here.
def index(request):
    # 首页
    typyinfo_list = TypeInfo.objects.all()

    ctx = {
        'typyinfo_list': typyinfo_list
    }

    return render(request, 'index.html', ctx)


def goods_list(request):
    # 列表页
    return render(request, 'list.html')
