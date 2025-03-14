from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_dish, name="add_dish"),
    path("list/", views.dish_list, name="dish_list"),
    path("update/<int:dish_id>/", views.update_dish, name="update_dish"),  # Update dish
    path("delete/<int:dish_id>/", views.delete_dish, name="delete_dish"),
    path("get-food-image/", views.get_food_image, name="get_food_image"),
]
