from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('load/', views.load_products, name='load_products'),
    path('product/<int:product_id>/', views.product, name='product'),
]