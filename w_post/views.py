from django.shortcuts import render,redirect
from .models import Post,Classify
from django.http import JsonResponse,HttpResponse
from my_core.jianshu import *
from threading import  Thread
from django.core.paginator import Paginator
from w_auth.user_decorator import is_login
# Create your views here.
def index(request):
    return render(request, 'post/index.html')

def get_post(request,slug):
    post = Post.my_objects.get_active_one(slug)
    context={'post':post,
             'title':post.title}
    return render(request,'post/detail.html',context)


@is_login
def write_post(request):
    uid = request.session.get('uid')
    try:
        cid = Classify.objects.filter(owner_id=int(uid)).first().id
    except:
        cid = None
    context = {'title':'写文章',
               'cid':cid}
    return render(request,'post/write.html',context)

def add_classify(request):
    uid = request.session.get('uid')
    if request.method=='GET':
        context={'title':'新建分类'}
        return render(request, 'post/new_classify.html',context)
    if request.method=='POST':
        title = request.POST.get('ctitle','')
        if title == '':
            return HttpResponse('不能为空')
        else:
            classify = Classify()
            classify.title =  title
            classify.owner_id = uid
            classify.save()
            return redirect('/write')

def add_post(request):
    uid = int(request.session.get('uid'))
    if request.method=='GET':
        c_l = Classify.objects.filter(owner_id=uid)
        context={'title':'新建分类',
                 'c_l':c_l}
        return render(request, 'post/new_post.html',context)
    if request.method=='POST':
        title = request.POST.get('ptitle','')
        cid = request.POST.get('cid','')
        if title == '' or cid =='':
            return HttpResponse('不能为空')
        else:
            post = Post()
            post.my_init(title,uid,'新文章内容',int(cid))
            post.save()
            return redirect('/write')

def update_post(request):
    if request.method == 'POST':
        id = int(request.POST.get('pid'))
        body = request.POST.get('body')
        post = Post.my_objects.get(id=id)
        if post.author_id == request.session.get('uid'):
            post.body=body
            post.save()
            context = {'title':'发布成功',
                       'post':post}
            return render(request,'post/success_post.html',context)


def splider_post(request):
    if request.method =='GET':
        return render(request,'post/splider.html')

    if request.method == 'POST':
        kw = request.POST.get('kw')
        start = int(request.POST.get('start'))
        end = int(request.POST.get('end'))
        t = Thread(target=manage,args=(start,end,kw))
        t.start()
        return redirect('/')

def jianshu(requst):
    try:
        kw = requst.GET.get('q')
        pindex = int(requst.GET.get('p'))
    except:
        kw = 'python'
        pindex =2
    kws = JianShuPost.objects.values('keyword').distinct()

    posts = JianShuPost.objects.filter(keyword=kw).all()
    try:
        paginator =Paginator(posts,10)
        page = paginator.page(pindex)
    except:
        paginator = None
        page = None
    context ={
        'title':'简书文章',
        'page':page,
        'paginator':paginator,
        'kw':kw,
        'kws':kws
    }
    return render(requst,'post/jianshu.html',context)

def jianshu_detail(request,slug):
    post = JianShuPost.objects.filter(slug=slug)[0]

    context = {
        'title':post.title,
        'post':post
    }
    return render(request,'post/jianshu_detail.html',context)

