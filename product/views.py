from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.views.generic import TemplateView, ListView, DetailView
from django.http import Http404



# view from here

# class HomeView(TemplateView):  # Home View 
#     template_name = "home.html"


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"
    context_object_name = "allproducts"
  
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-detail.html"
    queryset = Product.objects.all().featured()
    context_object_name = "allproducts"
  
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()
 


class ProductListView(ListView):
    template_name = "products/list.html"
    # queryset = Product.objects.all().order_by("-id")
    context_object_name = "allproducts"
  
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


class ProductDetailView(DetailView):
    template_name = "products/detail.html"
    # queryset = Product.objects.all()
    context_object_name = "allproducts"
   
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    ### Product manager
    def get_object(self, *args, **kwargs):   
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        # if instance is None:
        #     raise Http404("Product doesn't exist")
        # return instance
        try:
            instance = Product.objects.get(slug=slug, active=True)
            instance.view_count += 1
            instance.save()
        except Product.DoesNotExist:
            raise Http404("Product not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Looking...")
        return instance



    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     slug = self.kwargs.get('slug')
    #     return Product.objects.filter(slug=slug)



