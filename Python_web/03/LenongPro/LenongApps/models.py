from django.db import models


# Create your models here.
class TypeInfo(models.Model):
    """商品分类"""
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    """商品"""
    gtitle = models.CharField(max_length=20,verbose_name='商品名称')
    # 图片位置
    gpic = models.ImageField(verbose_name='图片位置',upload_to='df_goods')
    gprice = models.DecimalField(verbose_name='价格',max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    # 单位
    gunit = models.CharField(verbose_name='单位',max_length=20, default='500g')
    # 点击量  用于排序
    gclick = models.IntegerField()
    # 简介
    gjianjie = models.CharField(max_length=200,verbose_name='简介')
    # 库存
    gkucun = models.IntegerField(verbose_name='库存')
    # 详细介绍
    gcontent = models.TextField(verbose_name='详细介绍')
    #
    gtype = models.ForeignKey(TypeInfo,verbose_name='商品分类')

    def __str__(self):
        return self.gtitle
