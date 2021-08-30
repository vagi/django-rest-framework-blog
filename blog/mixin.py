from django.views.decorators.cache import cache_page


# This class implements cashing of choosen viewset with designed timeout
class CacheMixin(object):
    cache_timeout = 60 * 10

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(self.get_cache_timeout())(super(CacheMixin, self).dispatch)(*args, **kwargs)
