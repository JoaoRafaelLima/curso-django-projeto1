from django import forms 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import re

def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f"{existing_attr} {attr_new_val}".strip()

def add_placeholder(field, placeholder_val):
    add_attr(field, "placeholder", placeholder_val)
   
def strong_password(password):
    regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$")

    if not regex.match(password):
        raise ValidationError(
            (
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
            ),
            code="Invalide"
        )

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields["username"], "Your username")
        add_placeholder(self.fields["email"], "Your email")
        add_placeholder(self.fields["first_name"], "Ex.: John")
        add_placeholder(self.fields["last_name"], "Ex.: Doe")
        add_placeholder(self.fields["password"], "Type your password here")
        add_placeholder(self.fields["password2"], "Repeat your password here")
    username = forms.CharField(
        label="Username",
        help_text=(
            "Username must have letters, number or one of those  @.+-_ . ",
            "The length shold be between 4 and 150 characters."

        ),
        error_messages = {
            "required": "This field must be not empty",
            "min_length": "Username must have at least 4 characters",
            "max_length": "Username must have less then 150 characters"
        },
        min_length=4,
        max_length=150
    )
    first_name = forms.CharField(
        error_messages={
            "required": "Write your first name"
        },
        label="First name"
    )
    last_name = forms.CharField(
        error_messages={
            "required": "Write your last name"
        },
        label="Last name"
    )
    email = forms.EmailField(
        error_messages={
            "required": "Email is required"
        },
        label="E-mail",
        help_text = "email The e-mail must be a valid"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={}),
        error_messages={
            "required": "Password must not be empty"
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        validators=[
            strong_password
        ],
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={}),
        label="Password2",
        error_messages={
            "required": "Please, repeat your password"
        }
    )
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password"
            ]
        # exclude = ['first_name']
       
    
    def clean_email(self):
        email = self.cleaned_data.get("email", "")
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError("User e-mail already in use", code="invalid")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        password_confirmation_error = ValidationError(
            "Password and Password2 must be equal",
            code="invalid"
        )
        if password != password2:
            raise ValidationError({
                "password": password_confirmation_error,
                "password2": [
                    password_confirmation_error
                ]
            }
            )