from django.urls import path
from .views import (
    productListView,
    productDetailSlugView,
    )

app_name = 'products'
urlpatterns = [
    path('',productListView.as_view(), name='list'),
    # path('products/<pk>',productDetailSlugView.as_view()),
    path('<slug>',productDetailSlugView.as_view(), name='detail'),
]
