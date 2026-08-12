from rest_framework import serializers

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine


class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cuisine = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Restaurant(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cuisine = validated_data.get('cuisine', instance.cuisine)
        return instance
