from django.forms import ModelForm
from .models import Scraped
from django import forms

class RecipeForm(ModelForm):
    class Meta:
        model = Scraped
        fields = ('dish_name', 'full_sentence_ingredients', 'recipes', 'dish_img')
        labels = {
            'dish_name': '', 
            'full_sentence_ingredients': '',    
            'recipes': '',     
            'dish_img': '',     

        }
        widgets = {
            'dish_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dish name'}) ,  
            'full_sentence_ingredients': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingredients (eg: 1 Tbsp rice, 2 cloves garlic)'}) ,   
            'recipes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Recipe steps (Numerate your steps by leaving a comma at the end of the instruction eg: cook rice., cut fruits.,)'}) ,   
            
        }
       