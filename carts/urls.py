from django.conf.urls import url
from .views import *


app_name = "carts"

urlpatterns = [

    url(r'^$', cart_home ,name='home'),
    url(r'^update/$', cart_update ,name='update'),

]
