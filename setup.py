#!/usr/bin/env python
"""
Setup file for Sahcmo cart exchange package.
"""
import os
from distutils.core import setup

version = '.'.join(map(str, __import__('cart_exchange').VERSION))

setup(
    name='cart_exchange',
    version=version,
    description='Satchmo cart exchange',
    long_description = (
        "Satchmo cart exchange is an application for Satchmo framework based "
        "on Django that lets you save your cart's contents as one user and "
        "load as another one."),
    author='Stas Shtin',
    author_email='antisvin@gmail.com',
    url='http://code.google.com/p/satchmo-cart-exchange/',
    packages=[
        'cart_exchange',],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',        
    ),
)
