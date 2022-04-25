from rest_framework import serializers

from applications.cart.models import CartItem, Cart


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('product', 'quantity', 'total_cost')

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['product'] = f'{instance.product}'
    #     return representation

# {
#     "items": [
#         {
#         "product":"68",
#         "quantity":3
#         },
#         {
#         "product":"69",
#         "quantity":1
#         }
#     ]
# }

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, write_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'items', 'status')

    def create(self, validated_data):
        request = self.context.get('request')
        items = validated_data.pop('items')
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        for item in items:
            try:
                cart_item = CartItem.objects.get(cart=cart,
                                                 product=item['product'])
                cart_item.quantity = item['quantity']
            except CartItem.DoesNotExist:
                cart_item = CartItem(cart=cart, product=item['product'], quantity=item['quantity'])
            cart_item.save()
        return cart

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.email
        representation['products'] = CartItemSerializer(instance.cart_item.all(), many=True).data
        return representation
