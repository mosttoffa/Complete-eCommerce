from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from .views import HomeView



urlpatterns = [

    url(r'^$', HomeView.as_view(),name='home' ),

    url(r'^admin/', admin.site.urls),
    url(r'^product/', include('product.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^cart/', include('carts.urls')),

]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


