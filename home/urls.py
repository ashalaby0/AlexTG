from django.contrib.auth import views as auth_views
from django.urls import path

from home import views

urlpatterns = [
    # login/singup
    path(
        "password_reset",
        auth_views.PasswordResetView.as_view(
            template_name="password/password_reset.html"),
        name="password_reset"
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password/password_reset_confirm.html"),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    path(
        'contact_us',
        views.contact_us,
        name='contact_us'
    ),


    # home
    path(
        '',
        views.home,
        name='home'
    ),
    #booking
    path(
        'booking',
        views.booking,
        name='booking'
    ),
    #policy
    path(
        'policy',
        views.policy,
        name='policy'
    ),
    #faqs
    path(
        'faqs',
        views.faqs,
        name='faqs'
    ),
    #profile
    path(
        'profile',
        views.profile,
        name='profile'
    ),
    #setting
    path(
        'setting',
        views.setting,
        name='setting'
    ),

    path(
        'signup',
        views.signup_view,
        name='signup'
    ),

    path(
        'customer_messages',
        views.customer_messages,
        name='customer_messages'
    ),
    path(
        'close_customer_message',
        views.close_customer_message,
        name='close_customer_message'
    ),


]
