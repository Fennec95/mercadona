from django.test import TestCase
from django.contrib.auth import get_user_model
from store.models import Product


class UserTestCase(TestCase):
    def test_create_user(self):
        User = get_user_model()
        email = 'test@example.com'
        password = 'password123'
        user = User.objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

class ProductTestCase(TestCase):
    def test_create_product(self):
        product = Product.objects.create(name='Test Product', price=10)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 10)








