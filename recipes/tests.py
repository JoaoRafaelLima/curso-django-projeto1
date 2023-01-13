from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

# Create your tests here.

class RecipeURLsTest(TestCase):
    def test_recipe_home_ulr_is_correct(self):
        url = reverse("recipes:home")
        self.assertEqual(url, "/")

    def test_recipe_category_ulr_is_correct(self):
        url = reverse("recipes:category", args=(1,))
        self.assertEqual(url, "/recipes/category/1")

    def test_recipe_detail_ulr_is_correct(self):
        url = reverse("recipes:recipe", kwargs={"id": 1})
        self.assertEqual(url, "/recipes/1")

class RecipeViewsTest(TestCase):
    def teste_recipe_home_view_function_is_correct(self):
        view = resolve(reverse("recipes:home"))
        self.assertIs(view.func, views.home)

    def teste_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse("recipes:category", kwargs={"category_id":1})
            )
        self.assertIs(view.func, views.category)

    def teste_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse("recipes:recipe", kwargs={"id":1})
            )
        self.assertIs(view.func, views.recipe)