import json
import stripe 
import os

from django.shortcuts import render
from django.conf import settings

from django.http.response import HttpResponse

from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from basket.basket import Basket
from orders.views import payment_confirmation

from django.views.decorators.csrf import csrf_exempt



class Error(TemplateView):
    template_name = 'payment/error.hmtl'

def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')


@login_required
def basketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')

    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount = total,
        currency='gbp',
        metadata={'userid' : request.user.id}
    )

    context = {
        'client_secret': intent.client_secret, 
        'STRIPE_PUBLISHABLE_KEY':STRIPE_PUBLISHABLE_KEY
    }

    return render(request, 'payment/payment_form.html', context)



@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    print('payload', payload)
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)
    
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)
    
    else:
        print('Unhandled event type {}'.format(event.type))
    
    return HttpResponse(status=200)
