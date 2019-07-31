from django.urls import path
from .views import (
    product_create_view,
    product_detial_view
)

app_name = 'products'
urlpatterns = [
    path('', product_detial_view, name='product-detail'),
    path('create/', product_create_view, name='create')
]
