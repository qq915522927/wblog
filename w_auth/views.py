from django.shortcuts import render,redirect
from django.http import JsonResponse
from hashlib import sha1
from .models import User
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
        user.uemil = uemail
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