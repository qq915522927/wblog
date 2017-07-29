from django.db import models
from django.utils import  timezone
from w_auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
# Create your models here.
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(status='published').filter(isDelete=False)
    def get_active_one(self,slug):
        return  super(PostManager,self).filter(slug = slug).filter(status='published').filter(isDelete=False).first()

class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'),
                      ('published','Published'))

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish',null=True)
    author = models.ForeignKey('w_auth.User')
    image = models.CharField(max_length=200,default='')#封面图片地址
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
    choices = STATUS_CHOICES,default='draft')
    isDelete = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    click = models.IntegerField(default=0)#点击量
    support = models.IntegerField(default=0)#或赞数
    classify = models.ForeignKey('Classify')
    my_objects = PostManager()
    class Meta:
        ordering = ('-order','-publish')
    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):
        self.status='published'
        self.slug =slugify(str(datetime.now().timestamp())+str(self.title.encode('utf8')))
        return super(Post,self).save(*args,**kwargs)

    def seri(self):
        d = {'id':self.id,
            'title':self.title,
             'author':self.author.uname,
             'publish':self.publish.strftime('%Y/%M/%d'),
             'clik':self.click,
             'support':self.support,
             'body':self.body,
                'image':self.image,
             'slug':self.slug

             }
        return d

    def my_init(self,title,author_id,body,cid):
        self.title = title
        self.author_id = author_id
        self.body = body
        self.classify_id = cid
class Classify(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    def seri(self):
        d = {
            'id' : self.id,
            'title':self.title


        }
        return d

class JianShuPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    intro = models.CharField(max_length=500)
    datetime = models.DateTimeField()
    author_id=models.IntegerField()
    keyword = models.CharField(max_length=50,null=True)