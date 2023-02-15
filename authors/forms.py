from django import forms 
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f"{existing_attr} {attr_new_val}".strip()

def add_placeholder(field, placeholder_val):
    field.widget.attrs["placeholder"] = placeholder_val

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields["username"], "your username")
        add_placeholder(self.fields["email"], "your email")
        add_placeholder(self.fields["first_name"], "Ex.: John")
        add_placeholder(self.fields["email"], "EX.: Doe")

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
        "placeholder": "Your password here",
        })
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
        "placeholder": "Repeat your password here",
        })
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
        labels = {
            "username": "Username",
            "first_name": "First name",
            "last_name": "Last name",
            "email": "E-mail",
            "password": "Password",
        }
        help_texts = {
            "email": "The e-mail must be a valid"
        }
        error_messages = {
            "username": {
                "required": "This field must be not empty"
            }
        }
        widgets = {
            "first_name": forms.TextInput(attrs={
            "placeholder": "Type your name here",
            "class": ""
            }),
            "password": forms.PasswordInput(attrs={
            "placeholder": "Type your password here"
            })
        }
