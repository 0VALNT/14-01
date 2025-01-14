from django.urls import path
from .views import RecipeCreate, RecipeList, RecipeDetail, CookCreate, CookList, CookDetail

urlpatterns = [
    path('recipe/create', RecipeCreate.as_view(), name='recipe_create'),
    path('recipe/detail/<int:pk>', RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe/list', RecipeList.as_view(), name='recipe_list'),

    path('cook/create', CookCreate.as_view(), name='cook_create'),
    path('cook/detail/<int:pk>', CookDetail.as_view(), name='cook_detail'),
    path('cook/list', CookList.as_view(), name='cook_list'),
]

from .views import CookUpdate, RecipeUpdate, delete_recipe, delete_cook

urlpatterns += [
    path('recipe/delete/<int:pk>', delete_recipe, name='recipe_delete'),
    path('cook/delete/<int:pk>', delete_cook, name='cook_delete'),
    path('cook/update/<int:pk>', CookUpdate.as_view(), name='cook_update'),
    path('recipe/update/<int:pk>', RecipeUpdate.as_view(), name='recipe_update'),
]
