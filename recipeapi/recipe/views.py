from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from recipe.models import Recipe, Review
from recipe.serializers import UserSerializer, RecipeSerializer, ReviewSerializer


# Create your views here.

class Recipedetails(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class= RecipeSerializer

class Reviewrating(viewsets.ModelViewSet):
    # permission_classes= [IsAuthenticated]
    queryset= Review.objects.all()
    serializer_class= ReviewSerializer

class CreateUser(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class search(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if (query):
            recipe=Recipe.objects.filter(Q(name__icontains=query) | Q(ingredients__icontains=query))
            serialized_recipe=RecipeSerializer(recipe,many=True)
            return Response(serialized_recipe.data)
        else:
            return Response([])