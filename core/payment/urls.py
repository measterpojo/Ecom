
from django.urls import path 

from .views import basketView, order_placed, Error, stripe_webhook




urlpatterns = [

    path('', basketView, name='basket'),
    path('orderplaced/', order_placed, name='order_placed'),
    path('error/', Error.as_view(), name='error'),
    path('webhook/', stripe_webhook),

]