from django.urls import path 

from .views import product_detail, product_all, category_list

urlpatterns = [

    path('', product_all, name='home'),
    path('products/', product_all, name='home'),
    path('product/<slug:slug>',product_detail, name='detail'),
    path('catergory/<slug:category_slug>', category_list, name='category')

]