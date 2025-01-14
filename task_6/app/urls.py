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
