from django.db import models
from pytils.translit import slugify
import datetime

NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='Текст')
    blog_image = models.ImageField(upload_to='article/', **NULLABLE, verbose_name='Картинка')
    data_created = models.DateField(verbose_name='Дата создания', default='2023-01-01')
    data_published = models.DateField(verbose_name='Дата публикации', default='2023-01-01')
    number_views = models.IntegerField(verbose_name='Количество просмотров', default=0)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        """
        Добавление даты публикации и создания
        """
        if not self.slug:
            self.slug = slugify(self.title)
        now = datetime.datetime.now()
        self.data_created = now
        self.data_published = now
        super().save(args, kwargs)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
