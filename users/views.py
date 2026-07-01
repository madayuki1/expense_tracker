from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserRegisterForm
# Create your views here.


class RegisterView(CreateView):
    model = User
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("transaction_list")
