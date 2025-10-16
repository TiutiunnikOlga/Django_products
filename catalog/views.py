from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'

class  ProductViews(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
