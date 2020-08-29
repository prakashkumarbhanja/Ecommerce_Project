from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('product-detail-view/<str:slug>', ProductDetail.as_view(), name='product_detail_view'),
    path('search', search, name='search'),
]