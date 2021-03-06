from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Post,Classify
def post(request):
    '''
    根据页数，排序方式，所属分类来返回文章列表页，
    json格式返回
    p:页码
    c:所属分类id
    s:排序方式 1：按默认推荐排序，2：按时间排序，3：按欢迎度排序
    '''
    p = request.GET.get('p')
    c = request.GET.get('c')
    s = request.GET.get('s')
    if p is None:
        p = 1
    if c is None:
        c = 0
    if s is None:
        s = 1
    p=int(p)
    c=int(c)
    s=int(s)
    if c == 0:
        if s == 1:  # 按默认推荐排序
            posts = Post.my_objects.active()
        if s == 2:
            posts = Post.my_objects.active().order_by('-publish')
        if s ==3:
            posts = Post.my_objects.active().order_by('-click')

    paginator = Paginator(posts, per_page=5)
    page = paginator.page(p)

    l =[ post.seri() for post in page]

    d = {'posts':l}
    return JsonResponse(d)



def classify(request):
    u = request.GET.get('u')
    c_l= Classify.objects.filter(owner_id=int(u))

    l = [c.seri() for c in c_l]
    d = {'data':l}
    return JsonResponse(d)

def get_posts_by_cid(request,c):
    uid = request.session.get('uid')
    c = int(c)
    posts = Post.my_objects.filter(author_id=uid).filter(isDelete=False).filter(classify_id=c)
    l = [ p.seri() for p in posts]
    d = {'data':l}
    return  JsonResponse(d)

def get_post(request,pid):
    pid=int(pid)
    post = Post.my_objects.get(id=pid)
    d = post.seri()
    return JsonResponse(d)