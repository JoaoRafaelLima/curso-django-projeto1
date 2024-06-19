from .base import AuthorsBaseTest
import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By


@pytest.mark.functional_test
class AuthorLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = "myP@ass45"
        user = User.objects.create_user(username="my_user", password=string_password)
        self.browser.get(self.live_server_url + reverse("authors:login"))

        form = self.browser.find_element(By.CLASS_NAME, "main-form")
        username_field = self.get_element_by_placeholder(form, "Type your username")
        password_field = self.get_element_by_placeholder(form, "Type your password")

        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        form.submit()

        self.assertIn(
            "You are logged with my_user.",
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
        self.sleep()