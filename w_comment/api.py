from  django.http import JsonResponse
from .models import Comment


def get_comment_by_post(request,post_id):
    comments = Comment.objects.filter(post_id=post_id).all()
    count =  Comment.objects.filter(post_id=post_id).count()
    l = [comment.seria() for comment in comments]
    d = {'count':count,
        'comments':l}
    return JsonResponse(d)

def add_comment(request):
    if request.method=='POST':
        try:
            post=request.POST
            post_id = post.get('post_id')
            owner_user = post.get('owner_user')
            target_user = post.get('target_user_id')
            content = post.get('content')
            parent = post.get('parent')
            comment=Comment()
            comment.my_init(post_id,owner_user,target_user,content,parent)
            comment.save()
        except Exception as e:
            print(e)
            return  JsonResponse({'data':'False'})
        else:
            return JsonResponse({'data': 'True'})