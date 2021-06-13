from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList, name='api-products'),
    path('posts/', views.PostList, name='api-posts'),
    path('product/detail/<str:pk>/', views.ProductDetail, name='api-product-detail'),
    path('post/detail/<str:pk>/', views.PostDetail, name='api-post-dtail'),
    path('product/create/', views.ProductCreate, name='api-product-create'),
    path('post/create/', views.PostCreate, name='api-post-create'),
    path('product/update/<str:pk>/', views.ProductUpdate, name='api-product-update'),
    path('post/update/<str:pk>/', views.PostUpdate, name='api-post-update'),
    path('product/delete/<str:pk>/', views.ProductDelete, name='api-product-delete'),
    path('post/delete/<str:pk>/', views.PostDelete, name='api-post-delete'),
    
    
]
