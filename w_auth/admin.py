from django.contrib import admin
from .models import Role,User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['uname','role','uemail']
admin.site.register(Role)
admin.site.register(User,UserAdmin)
