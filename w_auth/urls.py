from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login$', views.login,name='login'),
    url(r'^register$', views.register,name='register'),
    url(r'^check_uname$', views.check_uname_is_exist,name='check_uname'),
    url(r'^logout$', views.logout,name='logout'),
    url(r'^user/base_info/(\d+)$', views.user_base_info,name='user_base_info'),
    url(r'^user/upload_avatar$', views.upload_avatar,name='upload_avatar'),
    url(r'^user/posts/(\d+)$', views.my_posts,name='my_posts'),


]