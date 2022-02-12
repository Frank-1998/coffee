from rest_framework import serializers
from . models import Coffee

# Serializer for list all coffees
class CoffeeSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ['id', 'name', 'price']

# retrive individual coffee details
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ['name', 'farm', 'region', 'fermentation', 'price']


# add coffee
class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ['id', 'name', 'farm', 'region', 'fermentation', 'price']
