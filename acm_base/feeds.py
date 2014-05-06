from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from news.models import *


class LatestEntriesFeed(Feed):
    title = "base.sdutacm.org latest news"
    link = "/news/"
    description = "Updates on changes and additions to base.sdutacm.org."

    def items(self):
        return News.objects.order_by('-publish_time')[:5]

    def item_title(self, item):
        return item.title

    # def item_description(self, item):
    #     return item.content

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return '/news/%d' % item.pk