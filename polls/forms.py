# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic.base import View
from django.contrib.auth import logout
from django import forms
from .models import Question


class RegisterFormView(FormView):

    form_class = UserCreationForm
    success_url = "/login"
    template_name = "polls/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):

    form_class = AuthenticationForm
    success_url = "test/"
    template_name = "polls/login.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("polls/login")


#{% url 'login' %}
