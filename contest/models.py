from django.db import models


class ContestList(models.Model):
    identifier = models.CharField(max_length=100, primary_key=True)

    def __unicode__(self):
        return u'%s' % (self.identifier, )


class Contest(models.Model):
    contest_name = models.CharField(max_length=100)
    identifier = models.ForeignKey(ContestList)
    introduction = models.TextField()
    award = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.contest_name,)