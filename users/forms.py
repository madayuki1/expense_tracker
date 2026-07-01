from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Column, Layout

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField(
    #     required=True,
    #     help_text= "150 characters or fewer. Letters, digits and @/./+/-/_ only."
    # )
    # first_name = forms.CharField(
    #     help_text="150 characters or fewer. Letters, digits and @/./+/-/_ only.", 
    #     max_length=150, 
    #     required=False
    # )
    # last_name = forms.CharField(
    #     help_text="150 characters or fewer. Letters, digits and @/./+/-/_ only.", 
    #     max_length=150, 
    #     required=False
    # )

    class Meta:
        model = User
        fields = [
            'username',
            # 'first_name',
            # 'last_name',
            # 'email',
            'password1',
            # 'password2'
        ]
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.layout = Layout(
            'username',
            # Row(
            #     Column('first_name'),
            #     Column('last_name')
            # ),
            # 'email',
            'password1',
            # 'password2'
        )