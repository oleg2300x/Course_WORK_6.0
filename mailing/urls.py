from django.urls import path
from mailing.views import MailingCreateView, MailingDetailView, MailingUpdateView, MailingDeleteView, MailingListView, mailing_go, mailing_finish, mailing_again, mailing_change_status

urlpatterns = [
    path('mailing_form/', MailingCreateView.as_view(), name='mailing_form'),
    path('mailing_info/<int:pk>', MailingDetailView.as_view(), name='mailing_info'),
    path('mailing_form/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing_list', MailingListView.as_view(), name='mailing_list'),
    path('mailing_go/<int:pk>', mailing_go, name='mailing_go'),
    path('mailing_finish/<int:pk>', mailing_finish, name='mailing_finish'),
    path('mailing_again/<int:pk>', mailing_again, name="mailing_again"),
    path('mailing_change_status/<int:pk>', mailing_change_status, name='mailing_change_status'),
]
