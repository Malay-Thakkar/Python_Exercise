from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    product_name=serializers.CharField(max_length=120)
    product_id=serializers.CharField(max_length=120)
    product_dict=serializers.CharField(max_length=120)
    product_price=serializers.CharField(max_length=120)
