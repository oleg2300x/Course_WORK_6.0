from django.db import models
from mailing.models import Mailing

NULLABLE = {'blank': True, 'null': True}
# Create your models here.


class Message(models.Model):
    """
    Модель сообщения
    """
    title = models.CharField(max_length=50, verbose_name='Название')
    body = models.TextField(verbose_name='Текст сообщения')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='ID Рассылки')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
