from django.conf.urls import url
from .views import *



app_name = "search"


urlpatterns = [

    url(r'^$', SearchProductView.as_view(),name='query'),
    # url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(),name='productsdetail'),
   
]
