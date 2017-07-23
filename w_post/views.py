from django.shortcuts import render
from .models import Post
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'post/index.html  ')

def get_post(request,slug):
    post = Post.my_objects.get_active_one(slug)
    context={'post':post,
             'title':post.title}
    return render(request,'post/detail.html',context)

