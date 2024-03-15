from django.contrib.auth.models import User
from rest_framework import serializers

from recipe.models import Recipe

from recipe.models import Review


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['name','ingredients','cuisine','meal_type','created_on','edited_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['recipe_id','user','rating','review','comment','created_at']

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['id','username','password']
    def create(self, validated_data):
        u=User.objects.Create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u