from django.urls import path
from recipes.views import *

app_name = "recipes"
urlpatterns = [
    path('', home, name="home"),
    path("recipes/search", search, name="search"),
    path("recipes/<int:id>", recipe, name="recipe"),
    path("recipes/category/<int:category_id>", category, name="category"),
]
