from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from base.models import Scraped

class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Scraped
        fields = '__all__'