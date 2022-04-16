
from django.contrib import admin
from django.urls import path
from pizza_app.views import PizzaLocations, PizzaPlaceOrder, PizzaStoreMenu

urlpatterns = [
    path('locations/', PizzaLocations.as_view()),
    path('store/<str:store_id>/menu', PizzaStoreMenu.as_view()),
    path('order', PizzaPlaceOrder.as_view())
]
