from django.contrib.auth import get_user_model
from django.db import models

from applications.product.models import Product

User = get_user_model()

class Cart(models.Model): # корзина
    CART_STATUS = (
        ('IN_PROCESSING', 'in_processing'),
        ('COMPLETED', 'completed'), # ЗАВЕРШЕННЫЙ
        ('DECLINED', 'declined') # ОТКЛОНЕННЫЙ
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    status = models.CharField(max_length=30, choices=CART_STATUS, default='in_processing')

    def __str__(self):
        return self.user.email
# 1
# name
# 10
#

# 1
# name2
# 3
#


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.PositiveIntegerField(default=1)
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.product} in {self.cart.id} cart'

    def save(self, *args, **kwargs):
        self.total_cost = self.product.price * self.quantity
        super(CartItem, self).save(*args, **kwargs)