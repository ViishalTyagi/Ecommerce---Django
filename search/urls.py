from django.urls import path

from .views import searchproductView

app_name = 'search'
urlpatterns = [
    path('',searchproductView.as_view(), name='query'),
]
