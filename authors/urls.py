from django.urls import path
from authors.views import *

app_name = "authors"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("register/create/", register_create, name="create"),
]
