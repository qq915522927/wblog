from django.conf.urls import url
from . import views
from . import api
urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/post$',api.post),
    url(r'^post/(.+)$',views.get_post)
]