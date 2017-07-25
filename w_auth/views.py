from django.shortcuts import render,redirect
from django.http import JsonResponse
from hashlib import sha1
from .models import User
from my_core.my_core import upload,del_upload
import os
from w_post.models import Post,Classify
# Create your views here.
def login(request):
    if request.method == 'GET':
        uname = request.COOKIES.get('uname', '')
        context = {'uname': uname,
                   'error': 0}
        try:
            url = request.META['HTTP_REFERER']
            print(url)
        except:
            url = '/'
        if url == 'http://'+request.META['HTTP_HOST'] +'/register' :
            url = request.COOKIES.get('url','/')
        response = render(request, 'w_auth/login.html', context)
        # render方法返回httpesponse方法
        response.set_cookie('url', url)
        return response


    if request.method == 'POST':
        # 接收表单数据
        post = request.POST
        uname = post.get('username')
        upwd1 = post.get('pwd')
        # 设置默认值
        # remember = post.get('remember', '0')

        # 加密
        s1 = sha1()
        s1.update(upwd1.encode('utf8'))
        upwd = s1.hexdigest()
        # 验证用户是否正确
        user = User.objects.filter(uname=uname).filter(upwd=upwd).first();

        if user:

            url = request.COOKIES.get('url', '/')  # 第二个参数为默认参数，如果url没有，则条首页
            red = redirect(url)
            # 如果记住密码则将用户名和密码写入cookies
            # if remember == '1':
            #
            #     red.set_cookie('uname', user.uname)
            #     red.set_cookie('upwd', upwd1)
            #
            # else:
            #     red.set_cookie('uname', '', max_age=-1)
            #     red.set_cookie('upwd', '', max_age=-1)
            #     # request.COOKIES['userinfo']=[user.uname,user.upwd]
            request.session['username'] = uname
            request.session['uid'] = user.id
            request.session['upic'] = user.avatar
            return red

        else:
            # 如果没有用户，怎返回错误参数
            context = {'error': 1,
                       'uname': uname}
            return render(request, 'w_auth/login.html', context)


def register(request):
    if request.method == 'GET':
        response = render(request, 'w_auth/register.html')
        try:
            url = request.META['HTTP_REFERER']
        except: url = '/'
        if url == 'http://' + request.META['HTTP_HOST'] + '/login':
            url ='/'
        response.set_cookie('url',url)
        return response
    if request.method == 'POST':
        # 接收用户输入
        post = request.POST
        uname = post.get('user_name')
        pwd = post.get('pwd')
        cpwd = post.get('cpwd')
        uemail = post.get('email')
        # allow = post.get('allow')
        # 判断密码是否相等
        if pwd != cpwd:
            return redirect('/user/register')
        # 存入数据库
        user = User()
        user.uname = uname
        user.upwd = pwd
        user.uemail = uemail
        user.hash_pwd()#自定义的方法
        user.save()

        return redirect('/login')
def logout(request):
    request.session.flush()  # 清空所有session
    return redirect('/')

def check_uname_is_exist(request):
    uname = request.GET.get('uname')  # 通过url传参的方式
    count = User.objects.filter(uname=uname).count()
    # print(count)
    # 返回json字典，判断是存在，
    return JsonResponse({'count': count})

def user_base_info(request,uid):
    if request.method == 'GET':
        uid = int(uid)
        user = User.objects.get(id=uid)

        context = {'title':'%s的个人信息'%user.uname,
                   'user':user,}
        return  render(request,'w_auth/base_info.html',context)
    if request.method == 'POST':
        uid = int(request.session.get('uid'))
        user = User.objects.get(id=uid)
        user.uemail = request.POST.get('uemail')
        user.save()
        return redirect('/user/base_info')


def upload_avatar(request):
    if request.method =='POST':
        file = request.FILES.get('avatar',None)

        name = upload(file)
        if name:
            uid=request.session.get('uid')
            user = User.objects.get(id=uid)
            del_upload(os.path.split(user.avatar)[1])
            user.avatar = '/static/upload/'+name
            user.save()
            return redirect('/user/base_info')

    return JsonResponse({'data':'false'})

def my_posts(request,uid):
    uid = int(uid)
    user = User.objects.get(id=uid)
    try:
        c = request.GET.get('c')
    except:
        pass
    if c:
        posts = Post.my_objects.filter(author_id=uid).filter(status='published').filter(isDelete=False).filter(classify_id=int(c))

    else:
        posts = Post.my_objects.filter(author_id=uid).filter(status='published').filter(isDelete=False)


    classifies = Classify.objects.filter(owner_id=uid)
    for classifiy in classifies:
        classifiy.pcount = classifiy.post_set.filter(author_id=uid).filter(status='published').filter(isDelete=False).count()
    context={'user':user,
             'posts':posts,
             'classifies':classifies,
             'pcount':len(posts),}

    return render(request,'w_auth/my_posts.html',context)