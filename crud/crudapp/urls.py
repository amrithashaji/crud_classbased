from django.contrib.auth import views
from django.urls import path
from django.views.generic.base import TemplateView
from . import views as asview

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('home/', TemplateView.as_view(template_name='registration/home.html'), name='home'), 
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    #have to add below to complete the reset
    # path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('contacts/', asview.ContactList.as_view(), name='contact_list'),
    path('contact/<int:pk>', asview.ContactDetail.as_view(), name='contact_detail'),
    path('create', asview.ContactCreate.as_view(), name='contact_create'),
    path('update/<int:pk>', asview.ContactUpdate.as_view(), name='contact_update'),
    path('delete/<int:pk>', asview.ContactDelete.as_view(), name='contact_delete'),
]