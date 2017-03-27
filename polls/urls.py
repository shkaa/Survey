# -*- coding:utf-8 -*-

from django.conf.urls import url
from .views import Testing, LoginFormView, RegisterFormView, ValidateQuestionAnswers
from .forms import logout
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^$', LoginFormView.as_view(), name='login'),
    url(r'^registration/$', RegisterFormView.as_view()),
    url(r'^registration/login/$', RegisterFormView.as_view()),
    url(r'^result/$', ValidateQuestionAnswers, name='result'),
    url(r'^login/test', Testing, name='test'),
    url(r'^test/', Testing, name='test'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'},
        name='logout'),
]
