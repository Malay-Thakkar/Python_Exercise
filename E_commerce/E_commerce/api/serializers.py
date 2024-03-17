from rest_framework import serializers
from api.models import ProductModel,CategoryModel

class CategorySerializers(serializers.HyperlinkedModelSerializer):
    category_id=serializers.ReadOnlyField()
    class Meta:
        model = CategoryModel
        fields="__all__"
        
class ProductSerializers(serializers.HyperlinkedModelSerializer):
    product_id=serializers.ReadOnlyField()
    class Meta:
        model = ProductModel
        fields="__all__"
        