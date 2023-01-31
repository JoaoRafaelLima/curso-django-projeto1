from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTesteBase
from unittest import skip


    
class RecipeHomeViewsTest(RecipeTesteBase):
        
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse("recipes:home"))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    @skip("WIP")
    def test_recipe_home_template_shows_no_recipe_if_no_recipe(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertIn(
            "No recipes found here.",
            response.content.decode('utf-8')
        )

        # Tenho que escrever mais alguma coisa
        self.fail("Para que eu termine de digitá-lo")
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse("recipes:home"))
        content = response.content.decode("utf-8")
        context_recipes = response.context['recipes']
        self.assertIn("Recipe Tilte", content)
        self.assertEqual(len(context_recipes), 1)
    
    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test Recipe is_published False dont show"""
        #need a recipe for this test
        self.make_recipe(is_published=False)
        response = self.client.get(reverse("recipes:home"))
        self.assertIn(
            "No recipes found here.",
            response.content.decode('utf-8')
        )