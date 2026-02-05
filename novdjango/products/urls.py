from django.urls import path
from . import views


urlpatterns = [
    # Define product-related URL patterns here
    path('',views.products, name='products'),
    path('product/',views.product, name='product'),
]