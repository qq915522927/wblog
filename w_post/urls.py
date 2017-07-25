from django.conf.urls import url
from . import views
from . import api
urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/post$',api.post),
    url(r'^post/([\w]+)$',views.get_post),
    url(r'^write$',views.write_post),
    url(r'^api/classify$',api.classify),
    url(r'^api/posts/(\d+)$',api.get_posts_by_cid),
    url(r'^api/post/(\d+)$',api.get_post),
    url(r'^add_c$',views.add_classify),
    url(r'^add_p$',views.add_post),
    url(r'^update_p$',views.update_post),

]