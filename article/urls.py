from django.urls import path
from article.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView
from django.views.decorators.cache import cache_page
from config.settings import CACHE_ENABLED

urlpatterns = [
    path('article_form/', ArticleCreateView.as_view(), name='article_form'),
    path('article_info/<slug:slug>/', ArticleDetailView.as_view(), name='article_info'),
    path('article_update/<slug:slug>/', ArticleUpdateView.as_view(), name='article_update'),
    path('article_delete/<slug:slug>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article_list', ArticleListView.as_view(), name='article_list')
]

