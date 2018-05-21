# from django.urls import path
# from . import views

#
# urlpatterns = [
    # path('remove/<product_id>/', views.cart_remove, name='cart_remove'),
    # path('add/<product_id>/', views.cart_add, name='cart_add'),
    # path('', views.cart_detail, name='cart_detail'),
from django.urls import re_path
from . import views
app_name='cart'

urlpatterns = [
    re_path(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    re_path(r'^$', views.CartDetail, name='CartDetail'),
]




