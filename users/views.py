from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


class RegisterView(CreateView):
    model = User
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("transaction_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        
        user = self.object 

        messages.success(self.request, f"Register Success, Welcome {user.username}") 
        return response

@login_required
def ProfileView(request):
    return render(request, 'users/profile.html')
    # model = User
    # template_name = "users/profile.html"