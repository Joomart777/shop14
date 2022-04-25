from django.contrib import admin

# Register your models here.
from applications.cart.models import *

admin.site.register(Cart)
admin.site.register(CartItem)

