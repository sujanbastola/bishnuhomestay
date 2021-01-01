from django.urls import path
from . import views



urlpatterns = [

    path('', views.roomdisplay, name='roomdisplay'),
    path('process_payment/', views.payment, name='payment'),
    path('checkoutok/<int:pk>/', views.checkout, name="checkout"),



]