from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('<int:id>/', views.orders, name='order-id')
]