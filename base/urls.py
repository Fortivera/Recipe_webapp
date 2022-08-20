from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name = 'home'),
    path('search/', views.searched_view, name = 'show_searched_page'),
    path('recipe-page/<pk>/', views.selected_recipe_view, name = 'show_selected_page' ),
    path('create-recipe/', views.create_recipe, name = 'show_create_recipe' ),   
]

 