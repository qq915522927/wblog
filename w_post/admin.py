from django.contrib import admin
from .models import *
# Register your models here.

#admin模型类，通过定义属性对admin界面的显示做设置
class PostAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['title','author','publish','status','isDelete']
admin.site.register(Post,PostAdmin)
admin.site.register(Classify)
