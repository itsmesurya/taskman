from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "task/signup.html"

class profile(TemplateView):
    template_name = "task/profile.html"
