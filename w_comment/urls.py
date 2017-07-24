from django.conf.urls import url
from . import views
from . import api

urlpatterns = [
    url(r'^api/comment/(\d+)$', api.get_comment_by_post),
    url(r'^api/comment$', api.add_comment),


]