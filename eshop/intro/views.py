from django.views.generic import DetailView
from django.shortcuts import render

from intro.models import Product


# Create your views here.
class ProductDetailView(DetailView):
    model = Product
