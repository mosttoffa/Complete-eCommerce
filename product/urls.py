from django.conf.urls import url
from .views import *


app_name = "product"

urlpatterns = [

    url(r'^$', HomeView.as_view(),name='home'),
    url(r'^products/$', ProductListView.as_view(),name='products'),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(),name='productsdetail'),
    
]
