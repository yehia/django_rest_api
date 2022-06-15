from rest_framework import serializers
from rest_framework.reverse import reverse
from .validators import unique_product_title
from api.serializers import UserPublicSerializer
from .models import Product, User

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )
    title = serializers.CharField(validators=[unique_product_title])

    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'id',
            'title',
            'content',
            'price', 
            'sale_price', 
            'owner',
        ]

    # def get_my_user_data(self, obj):
    #     return {
    #         'username': obj.user.username,
    #     }

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already a product name')
    #     return value

    # def create(self, validated_data):
    #     #return Product.objects.create(**validated_data)
    #     email = validated_data.pop('email')
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     return instance

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)

    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()