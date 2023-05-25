from django.conf.urls import url
from django.urls import re_path, path
from .views.brand.views import *
from .views.category.views import *
from .views.product.views import *

urlpatterns = [
    # brand
    path('brand/', BrandListView.as_view(), name='brand_list'),
    path('brand/add/', BrandCreate.as_view(), name='brand_create'),
    path('brand/update/<int:pk>/', BrandUpdate.as_view(), name='brand_update'),
    path('brand/delete/<int:pk>/', BrandDelete.as_view(), name='brand_delete'),
    # category
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreate.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDelete.as_view(), name='category_delete'),
    # product
    re_path(r'^$', ProductListView.as_view(), name='product_list'),
    path('add/', ProductCreate.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='product_delete'),
]