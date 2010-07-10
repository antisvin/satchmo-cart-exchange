from django.conf.urls.defaults import *

urlpatterns = patterns(
    'cart_exchange.views',
    url('^save/$', 'cart_save', name='cart-save'),
    url('^save/failed/$', 'cart_not_found', name='cart-not-found'),
    url('^saved/(?P<cart_id>\d+)/(?P<cart_hash>\d+)/$', 'cart_saved',
        name='cart-saved'),
    url('^load/(?P<cart_id>\d+)/(?P<cart_hash>\d+)/$', 'cart_load',
        name='cart-load'),
    )
    
