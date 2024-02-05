from article.models import Article
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from article.forms import ArticleForm
from config.settings import CACHE_ENABLED
from django.core.cache import cache


class ArticleCreateView(PermissionRequiredMixin, CreateView):
    """
    Создание новой статьи
    """
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_form.html'
    permission_required = 'article.change_article'

    def get_success_url(self):
        return reverse('article_info', args=[self.object.slug])


class ArticleDetailView(DetailView):
    """
    Детали статьи
    """
    model = Article
    template_name = 'article/article_info.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.number_views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)

        return self.render_to_response(context)


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Удаление статьи
    """
    model = Article
    template_name = 'article/article_confirm_delete.html'
    success_url = reverse_lazy('index')
    permission_required = 'article.change_article'


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Изменение статьи
    """
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_form.html'
    permission_required = 'article.change_article'

    def get_success_url(self):
        return reverse('article_info', args=[self.object.slug])


class ArticleListView(ListView):
    """
    Просмотр списка статей
    """
    model = Article
    template_name = 'article/article_list.html'

    def get_queryset(self):
        """
        Проверка прав для просмотра неопубликованных статей
        """
        if CACHE_ENABLED:
            key = 'article_list'
            articles = cache.get(key)
            if articles is None:
                articles = super().get_queryset()
                cache.set(key, articles)
        else:
            articles = super().get_queryset()
        if self.request.user.has_perm('article.change_article'):
            return articles
        return articles.filter(is_published=True)
