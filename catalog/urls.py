from django.urls import path
from catalog.apps import ProductsConfig
from catalog.views import home, contacts

app_name = ProductsConfig.name

urlpatterns = [
    path('home/',home, name='home'),
    path('contacts/',contacts, name='contacts')
]
