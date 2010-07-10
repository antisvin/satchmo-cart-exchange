from django.conf import settings
from hashlib import md5

def make_hash(cart):
    return md5(settings.SECRET_KEY + str(cart.id)).hexdigest()
