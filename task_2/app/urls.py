from django.urls import path
from .views import RecipeCreate, RecipeList, RecipeDetail, IngredientCreate, IngredientList, IngredientDetail

urlpatterns = [
    path('recipe/create', RecipeCreate.as_view(), name='recipe_create'),
    path('recipe/detail/<int:pk>', RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe/list', RecipeList.as_view(), name='recipe_list'),

    path('ingredient/create', IngredientCreate.as_view(), name='ingredient_create'),
    path('ingredient/detail/<int:pk>', IngredientDetail.as_view(), name='ingredient_detail'),
    path('ingredient/list', IngredientList.as_view(), name='ingredient_list'),
]
from .views import RecipeUpdate, IngredientUpdate, delete_ingredient, delete_recipe

urlpatterns += [
    path('ingredient/delete/<int:pk>', delete_ingredient, name='ingredient_delete'),
    path('recipe/delete/<int:pk>', delete_recipe, name='recipe_delete'),
    path('recipe/update/<int:pk>', RecipeUpdate.as_view(), name='ingredient_update'),
    path('ingredient/update/<int:pk>', IngredientUpdate.as_view(), name='recipe_update'),
]
