from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView


from .models import Product



# view from here

class HomeView(TemplateView):  # Home View 
    template_name = "home.html"


class ProductListView(ListView):
    template_name = "products/list.html"
    queryset = Product.objects.all().order_by("-id")
    context_object_name = "allproducts"
  
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context



class ProductDetailView(DetailView):
    template_name = "products/detail.html"
    queryset = Product.objects.all()
    context_object_name = "allproducts"
   
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context



