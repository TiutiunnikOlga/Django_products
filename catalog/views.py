from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from catalog.sevices import get_product_from_cache, ProductService


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'

class  ProductViews(ListView):
    model = Product

    def get_queryset(self):
        return get_product_from_cache()

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

    def form_valid(self):
        user = self.request.user
        product = self.get_object()
        return user == product.owner or user.has_perm('catalog.can_unpublish_product')


class ProductCategoryListView(ListView):
    model = Product
    template_name = "catalog/product_catalog.html"
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            id=self.kwargs['category_id']
        )
        cache_key = f'products_category_{self.category.id}'
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return cached_data
        queryset = Product.objects.filter(category=self.category)
        queryset = queryset.select_related('category')
        result = list(queryset)
        cache.set(cache_key, result, 60)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
