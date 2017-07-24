from django.db import models
from w_auth.models import User
from markdown import markdown
# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey('w_post.Post')
    owner_user = models.ForeignKey('w_auth.User')
    target_user = models.IntegerField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('Comment', null=True)
    #
    def my_init(self,post_id,owner_user_id,target_user,content,parent_id,*args):
        self.post_id = post_id
        self.owner_user_id = owner_user_id
        self.target_user = target_user
        self.content = content
        self.parent_id = parent_id



    def __str__(self):
        return self.post.title[0:10] + '...'
    def seria(self):
        d = {
            'id' :self.id,
            'post':self.post_id,
            'owner_user':[self.owner_user_id,self.owner_user.uname],
            'target_user':[self.target_user,User.objects.get(id=self.target_user).uname],
            'content':markdown(self.content),
            'created':self.created,
            'parent':self.parent_id
        }

        return d