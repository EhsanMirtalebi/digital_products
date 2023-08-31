from rest_framework import serializers

from .models import Category,Product,File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id','title', 'file')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)
    # foo = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('id','title', 'description', 'avatar', 'categories', 'files', 'url')

    # def get_foo(self,obj):
    #     return obj.id
