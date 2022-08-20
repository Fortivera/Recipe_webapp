
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Scraped
from .serializers import RecipeSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/recipes',
        'GET /api/recipes/:pk',
    ]
    return Response(routes)

@api_view(['GET'])
def getRecipes(request):
    recipes = Scraped.objects.all()
    serializer = RecipeSerializer(recipes,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getRecipe(request, pk):
    recipe = Scraped.objects.get(pk=pk)
    serializer = RecipeSerializer(recipe,many = False)
    return Response(serializer.data)