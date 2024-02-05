from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True }


# Create your models here.
class User(AbstractUser):
    """
    Модель пользователя
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE)
    lastname = models.CharField(max_length=50, verbose_name='Фамилия', **NULLABLE)
    company = models.CharField(max_length=50, verbose_name='Компания', **NULLABLE)
    avatar = models.ImageField(upload_to='users', **NULLABLE, verbose_name='Фото')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    birthday = models.DateField(verbose_name='Дата рождения', **NULLABLE)
    comment = models.CharField(max_length=300, verbose_name='Коментарий', **NULLABLE)
    is_manager = models.BooleanField(default=False)
    email_verify = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
