from django.shortcuts import render,redirect
from .models import Post,Classify
from django.http import JsonResponse,HttpResponse


# Create your views here.
def index(request):
    return render(request, 'post/index.html  ')

def get_post(request,slug):
    post = Post.my_objects.get_active_one(slug)
    context={'post':post,
             'title':post.title}
    return render(request,'post/detail.html',context)

def write_post(request):
    uid = request.session.get('uid')
    cid = Classify.objects.filter(owner_id=int(uid)).first().id
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