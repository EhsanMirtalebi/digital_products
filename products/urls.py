from django.urls import path
from .views import (
    ProductListView, ProductDetailView, CategoryDetailView, CategoryListView,FileListView,FileDetailView
)


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('products/',ProductListView.as_view(),name='products-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:product_id>/files/', FileListView.as_view(), name='file-list'),
    path('products/<int:product_id>/files/<int:pk>/', FileDetailView.as_view(), name='file-detail')
]

