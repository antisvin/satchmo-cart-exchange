from django import http
from django.core.urlresolvers import reverse
from satchmo_store.shop import models


def cart_save(request):
    try:
        # Look for cart in current request, but don't create it if it's not
        # available.
        cart = models.Cart.objects.from_request(
            request, create=False, return_nullcart=False)
        if cart.is_empty:
            raise models.Cart.DoesNotExist()
        
    except models.Cart.DoesNotExist:
        # Cart not found or empty, redirect to error page.
        return http.HttpResponseRedirect(reverse('cart-not-found'))

    else:
        # Cart found, redirect to info page.
        return http.HttpResponseRedirect(
            reverse('cart-saved', args=[cart.id, make_hash(cart)]))

def cart_not_found(request):
    pass

def cart_saved(request, cart_id, cart_hash):
    pass

def cart_load(request, cart_id, cart_hash):
    pass
