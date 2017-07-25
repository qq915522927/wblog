from django.db import models
from  hashlib import sha1
# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    role = models.ForeignKey('w_auth.Role',default='1')
    avatar = models.CharField(max_length=150,default='',null=True)

    def __str__(self):
        return self.uname
    def hash_pwd(self):
        # 密码加密
        # 使用sha1加密
        s1 = sha1()
        # sha1加密前，要先编码为比特
        s1.update(self.upwd.encode('utf8'))
        self.upwd = s1.hexdigest()


class Role(models.Model):
    rtitle = models.CharField(max_length=20,default='未激活用户')
    power = models.IntegerField(default=0)#用户所在组的权限

