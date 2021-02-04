from django.shortcuts import render
from product.models import Product
from django.views.generic import ListView

# Create your views here.


class SearchProductView(ListView):
    template_name = "search/view.html"
    context_object_name = "allproducts"
  
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q]
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
     
            
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''

    