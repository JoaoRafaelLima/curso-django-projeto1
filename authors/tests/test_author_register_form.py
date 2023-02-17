#from django.test import TestCase
from unittest import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ("username", "Your username"),
        ("email", "Your email"),
        ("first_name", "Ex.: John"),
        ("last_name", "Ex.: Doe"),
        ("password", "Type your password here"),
        ("password2", "Repeat your password here"),
    ])
    def test_fields_placeholder(self, field, placeholder):
        #test_first_name_placeholder_is_correct
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs["placeholder"]
        self.assertEqual(placeholder, current_placeholder)

    @parameterized.expand([
        ("password",
            (
                'Password must have at least one uppercase letter, '
                'one lowercase letter and one number. The length should be '
                'at least 8 characters.'
            ),
        ),
        ("email", "The e-mail must be a valid"),
        ("username", "Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.")
    ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text

        self.assertEqual(current, needed)
    
    @parameterized.expand([
        ("username", "Username"),
        ("email", "E-mail"),
        ("first_name", "First name"),
        ("last_name", "Last name"),
        ("password", "Password"),
        ("password2", "Password2"),
    ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label

        self.assertEqual(current, needed)