from django.urls import path
from catalog.apps import ProductsConfig
from catalog.views import home, contacts, product_detail


app_name = ProductsConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path('product/<int:pk>/', product_detail, name='product_detail')
]
