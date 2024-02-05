from django.urls import path
from django.views.generic import TemplateView
from users.views import UserUpdateView, RegisterView, EmailVerify, LoginView, LogoutView, forgot_password, \
    user_profile, moderator_users, user_change_active

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_update/', UserUpdateView.as_view(), name='user_update'),
    path('profile/<int:pk>', user_profile, name='profile'),
    path('forgot/', forgot_password, name='forgot'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'), name='confirm_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'), name='invalid_verify'),
    path('all_users/', moderator_users, name='moderator_users'),
    path('user_deactivate/<int:pk>', user_change_active, name='user_change_active'),
]
