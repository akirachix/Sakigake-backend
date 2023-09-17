from django.urls import path

from .views import ShopDetailView, ShopView




urlpatterns = [
    path('shops/', ShopView.as_view() , name="shop"),
    path('shops/<int:id>/',ShopDetailView.as_view() , name="shop_detail"), 
]

