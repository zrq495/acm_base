from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.ImageField(upload_to='./image/')
    description = models.TextField(blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' %(self.image_name)

    class Meta:
        ordering = ['-upload_time']