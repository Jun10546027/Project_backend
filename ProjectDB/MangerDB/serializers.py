from django.core import  serializers

from .models import Item

data = serializers.serialize("json",Item.objects.all(),fields=('id','title','MyClass','content'))


from rest_framework import serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('url','id','title','MyClass','content')