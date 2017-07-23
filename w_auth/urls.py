from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login$', views.login,name='login'),
    url(r'^register$', views.register,name='register'),
    url(r'^check_uname$', views.check_uname_is_exist,name='check_uname'),
    url(r'^logout$', views.logout,name='logout'),

]