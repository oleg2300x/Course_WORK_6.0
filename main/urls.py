from django.urls import path
from main.views import index
from article.views import ArticleCreateView
from django.views.decorators.cache import cache_page
from config.settings import CACHE_ENABLED

urlpatterns = []

if CACHE_ENABLED:
    urlpatterns.append(path('', cache_page(60)(index), name='index'))
else:
    urlpatterns.append(path('', index, name='index'))

