from django.http import  HttpResponseRedirect

def is_login(func):

    def wrap(request,*args,**kwargs):
        if request.session.has_key('uid'):
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/login')
            # 将当前页的url存入cookie

            red.set_cookie('url', request.get_full_path())

            return red




    return wrap