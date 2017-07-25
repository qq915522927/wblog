import os
import time
from wblog.settings import STATICFILES_DIRS
def upload(file):

    name= file.name
    extentions=os.path.splitext(name)[1]
    firstname=time.strftime('%Y%m%d%H%M%S')
    name=firstname+extentions
    os.chdir( os.path.join(STATICFILES_DIRS[0],'upload'))
    with open(name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return name

def del_upload(filename):
    os.chdir(os.path.join(STATICFILES_DIRS[0], 'upload'))
    if os.path.exists(filename):
        os.remove(filename)