"""
Test for satchmo cart exchange.
"""
from django.core.urlresolvers import reverse
from django.test import TestCase
from satchmo_store.shop import models


class ExchangeTest(TestCase):
    fixtures = 'sample-store-data.yaml', 'test-config.yaml'
    
    def test_cart_save(self):
        """
        Tests cart saving.
        """
        cart = models.Cart()
        self.client.get(reverse('cart_exchange.views.cart_save'))

    def test_cart_not_found(self):
        """
        Test cart not found page gets displayed.
        """
        raise NotImplementedError

    def test_cart_saved(self):
        """
        Tests view displayed after saving cart.
        """
        raise NotImplementedError

    def test_cart_load(self):
        """
        Tests loading cart.
        """
        raise NotImplementedError
