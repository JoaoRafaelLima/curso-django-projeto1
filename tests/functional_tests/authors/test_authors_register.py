from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest

@pytest.mark.functional_test
class AuthorsRegisterTest(AuthorsBaseTest):
    def fill_form_dummy_data(self, form):
        fields = form.find_elements(
            By.TAG_NAME, "input"
        )
        for field in fields:
            if field.is_displayed():
                field.send_keys(" " * 20)
    
    def get_form(self):
        form = self.browser.find_element(By.XPATH, "/html/body/main/div[2]/form")
        return form
    
    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + "/authors/register/")
        form = self.get_form()
        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, "email").send_keys("dummy@email.com")
        callback(form)

        return form

    def test_empty_first_name_error_message(self):
        def callback(form):
            first_name_field = self.get_element_by_placeholder(form, "Ex.: John")
            first_name_field.send_keys(" ")
            first_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn("Write your first name", form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_last_name_error_message(self):
        def callback(form):
            last_name_field = self.get_element_by_placeholder(form, "Ex.: Doe")
            last_name_field.send_keys(" ")
            last_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn("Write your last name", form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_username_error_message(self):
        def callback(form):
            last_name_field = self.get_element_by_placeholder(form, "Your username")
            last_name_field.send_keys(" ")
            last_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn("This field must be not empty", form.text)
        self.form_field_test_with_callback(callback)

    def test_invalid_email_error_message(self):
        def callback(form):
            email_field = self.get_element_by_placeholder(form, "Your email")
            email_field.send_keys("email@invalid")
            email_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn("The e-mail must be a valid", form.text)
        self.form_field_test_with_callback(callback)

    def test_passwords_do_not_match(self):
        def callback(form):
            password1 = self.get_element_by_placeholder(form, "Type your password here")
            password2 = self.get_element_by_placeholder(form, "Repeat your password here")
            password1.send_keys("P@ssw0rd")
            password2.send_keys("P@ssw0rd_Different")
            password2.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn("Password and Password2 must be equal", form.text)
        self.form_field_test_with_callback(callback)
    
    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + "/authors/register")
        form = self.get_form()
        self.get_element_by_placeholder(form, "Ex.: John").send_keys("João")
        self.get_element_by_placeholder(form, "Ex.: Doe").send_keys("Rafael")
        self.get_element_by_placeholder(form, "Your username").send_keys("joaorafaelteste")
        self.get_element_by_placeholder(form, "Your email").send_keys("email@deteste.com")
        self.get_element_by_placeholder(form, "Type your password here").send_keys("senha01FF@")
        self.get_element_by_placeholder(form, "Repeat your password here").send_keys("senha01FF@")

        form.submit()
        self.assertIn(
            "your user is created, please log in",
            self.browser.find_element(By.TAG_NAME, "Body").text
        )
