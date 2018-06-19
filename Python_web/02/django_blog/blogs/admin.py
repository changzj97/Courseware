from django.contrib import admin
from .models import Banner, Post, BlogCategory, Tags, FriendlyLink,Comment

# Register your models here.

admin.site.register(Banner)
admin.site.register(Post)
admin.site.register(BlogCategory)
admin.site.register(Tags)
admin.site.register(FriendlyLink)
admin.site.register(Comment)
