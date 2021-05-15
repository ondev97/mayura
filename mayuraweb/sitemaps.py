from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from decouple import config
from mayuraweb.models import BlogPost


class BlogSitemap(Sitemap):
    changefreq = config('CHANGE_FREQ', cast=str)
    priority = config('PRIORITY', cast=float)
    protocol = config('PROTOCOL', cast=str)
    def items(self):
        return BlogPost.objects.all()
    def lastmod(self, obj):
        return obj.date

    def location(self,obj):
        return '/blogpost/%s' % (obj.slug)

class StaticSitemap(Sitemap):
    changefreq = config('CHANGE_FREQ', cast=str)
    priority = config('PRIORITY', cast=float)
    protocol = config('PROTOCOL', cast=str)
    def items(self):
        return ['index','blog', 'contact', 'who_are_we']
    def location(self, item):
        return reverse(item)
