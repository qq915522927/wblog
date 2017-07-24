from django.contrib import admin
from .models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','content','owner_user','target_user','created','parent','post']

admin.site.register(Comment,CommentAdmin)