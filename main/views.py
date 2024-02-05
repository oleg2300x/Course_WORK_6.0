from django.shortcuts import render
from article.models import Article
from users.models import User
from mailing.models import Mailing
from client.models import Client
import random


# Create your views here.
def index(request):
    """
    Домашняя страница с 3 случайными статьями
    """
    articles = Article.objects.all()
    if len(articles) > 0:
        data = {
            'article_1': random.choice(articles),
            'article_2': random.choice(articles),
            'article_3': random.choice(articles),
        }
    else:
        data = {}
    data["number_users"] = len(User.objects.all())
    data["number_mailings"] = len(Mailing.objects.filter(status='Finished').all())
    data["number_clients"] = len(Client.objects.all())

    return render(request, 'main/index.html', context=data)
