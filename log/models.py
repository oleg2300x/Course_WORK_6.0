from django.db import models
from mailing.models import Mailing

NULLABLE = {'blank': True, 'null': True}
# Create your models here.


class Log(models.Model):
    """Модель Логов"""
    datatime = models.DateTimeField(verbose_name='Дата и время')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='ID Рассылки')
    status = models.CharField(max_length=150, verbose_name='Статус')
    answer_mail_server = models.TextField(verbose_name='Ответ сервера')

    def __str__(self):
        return f'{self.datatime} {self.mailing}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
