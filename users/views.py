from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from users.models import User
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from users.forms import UserRegisterForm, UserForm, AuthenticationForm
from users.utils import send_email_for_verify
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth import login
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
import random
from mailing.utils import sorting_list_mailings


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm


class EmailVerify(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('index')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


class LogoutView(BaseLogoutView):
    """
    Выход из системы
    """
    pass


class RegisterView(CreateView):
    """
    Регистрация нового пользователя
    """
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_email_for_verify(self.request, new_user)
        return redirect(reverse('login'))


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """
    Изменения данных пользователя
    """
    model = User
    success_url = reverse_lazy('user_update')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


@permission_required('mailing.change_mailing')
def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    mailing_list = sorted(Mailing.objects.filter(user=user).all(), key=lambda object: object.pk,
                          reverse=True)
    context = sorting_list_mailings(mailing_list)
    context["object"] = user
    return render(request, 'users/user_info.html', context)


def forgot_password(request):
    """
    Сброс пароля
    """
    if request.method == 'POST':
        email = request.POST.get('user_email')
        try:
            user = User.objects.get(email=email)
            new_password = ''.join([str(random.randint(0, 9)) for _ in range(8)])
            send_mail(
                subject='New password',
                message=f'Your new password {new_password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            user.set_password(new_password)
            user.save()
            return redirect(reverse('login'))
        except Exception:
            message = 'We can not find user with this email'
            context = {
                'message': message
            }
            return render(request, 'users/forgot_password.html', context)
    else:
        return render(request, 'users/forgot_password.html')


@permission_required('mailing.change_mailing')
def moderator_users(request):
    users = User.objects.all()
    objects = []
    for user in users:
        number_of_mailings = len(Mailing.objects.filter(user=user).all())
        objects.append({"user": user, "number_of_mailings": number_of_mailings})
    context = {
        "objects": objects
    }
    return render(request, 'users/moderator_users.html', context)


@permission_required('mailing.change_mailing')
def user_change_active(request, pk):
    user = User.objects.get(pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect(request.META.get('HTTP_REFERER'))
