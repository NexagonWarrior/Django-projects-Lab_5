from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # список блогів
    path('<int:pk>/', views.product_detail, name='product_detail'),  # деталі блогу
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),  # редагування
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),  # видалення
]
