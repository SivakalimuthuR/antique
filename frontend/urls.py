from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('details',views.details, name='details'),
    # path('details/<int:pk>/', views.product_detail, name='product_detail'),
    path('post-product/', views.post_product, name='post_product'),
]