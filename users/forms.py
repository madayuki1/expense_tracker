from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text= "150 characters or fewer. Letters, digits and @/./+/-/_ only."
    )
    first_name = forms.TextInput(
        required=True,
        help_text= "150 characters or fewer. Letters, digits and @/./+/-/_ only."
    )
    last_name = forms.TextInput(
        required=True,
        help_text= "150 characters or fewer. Letters, digits and @/./+/-/_ only."
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]