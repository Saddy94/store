from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls'), namespace='cart')),
    path('shop/', include(('shop.urls'), namespace='shop')),
    path('', include('homepage.urls')),
    path('', include('login.urls')),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
