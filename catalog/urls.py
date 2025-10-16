from django.urls import path
from catalog.apps import ProductsConfig
from catalog.views import ProductViews, ProductDetailView, ContactView

app_name = ProductsConfig.name

urlpatterns = [
    path("home/", ProductViews.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
