from unittest import skip

from accounts.models import Account
from django.http import HttpRequest, request, response
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from ..models import Category, Product
from ..views import product_all


@skip("demonstrarting skipping")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponse(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Account.objects.create(name='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners',
         created_by_id=1,slug='django-beginners', price='20.00', image='django')

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/products/')

        self.assertEqual(response.status_code, 200)
    
    def test_product_list_url(self):
        """
        Test category response status
        """
        response = self.c.get(
            reverse('category', args=['django'])
        )
        self.assertEqual(response.status_code, 200)
    
    def test_product_detail_url(self):
        """
        Test category response status
        """
        response = self.c.get(
            reverse('detail', args=['django-beginners'])
        )
        self.assertEqual(response.status_code, 200)
    
