from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.ShowProducts.as_view(), name='ShowProducts'),
]