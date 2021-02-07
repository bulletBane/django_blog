from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def lastmod(self, obj):
        return obj.updated

    def items(self):
        return Post.published.all()
