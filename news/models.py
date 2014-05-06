# coding = utf-8

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #author = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    display = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' %(self.title)

    class Meta:
        ordering = ['-publish_time']