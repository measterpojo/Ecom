from accounts.models import Account

from django.test import TestCase
from django.urls import reverse

from ..models import Category, Product



class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')
    
    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data = self.data1
        response = self.client.post(
            reverse('category', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

class TestProductModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        Account.objects.create(name='admin')

        self.data1 = Product.objects.create(category_id=1, 
        title='django beginners', created_by_id=1,
        slug='django-beginners', price='20.00')

        self.data2 = Product.objects.create(category_id=1, 
        title='django advanced', created_by_id=1,
        slug='django-advanced', price='20.00', is_active=False)
    

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')
    
    def test_products_url(self):
        """
        Test product model slug and URL reverse
        """
        data = self.data1
        url = reverse('detail', args=[data.slug])
        self.assertEqual(url, '/product/django-beginners')

        response = self.client.post(
            reverse('detail', args=[data.slug]))
        self.assertEqual(response.status_code, 200)
    
    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        data = Product.products.all()
        self.assertEqual(data.count(), 1)


