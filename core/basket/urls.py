from django.urls import path

from .views import (basket_add, 
    basket_delete, basket_summary,
     basket_update)
    

urlpatterns = [
    path('', basket_summary, name='basket_summary'),
    path('add/', basket_add, name='basket_add'),
    path('delete/', basket_delete, name='basket_delete'),
    path('update/', basket_update, name='basket_update'),
]
