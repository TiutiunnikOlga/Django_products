from django.urls import path
from catalog.apps import ProductsConfig
from catalog.views import (
    ProductViews,
    ProductDetailView,
    ContactView,
    ProductUpdateView,
    ProductCreateView,
    ProductDeleteView,
    ProductCategoryListView,
)

app_name = ProductsConfig.name

urlpatterns = [
    path("home/", ProductViews.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path(
        "product_catalog/<int:category_id>/",
        ProductCategoryListView.as_view(),
        name="product_catalog",
    ),
]
