from django.urls import path
from .views import (
    productListView,
    productDetailSlugView,
    )

urlpatterns = [
    path('',productListView.as_view()),
    # path('products/<pk>',productDetailSlugView.as_view()),
    path('<slug>',productDetailSlugView.as_view(), name='detail'),
]
