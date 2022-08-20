from multiprocessing import context
from django.shortcuts import render
from .models import Scraped
from django.contrib.postgres.search import SearchVector, SearchQuery
from .forms import RecipeForm
from django.shortcuts import redirect

def home(request):
    data = Scraped.objects.all()
    context = {'data': data }
    return render (request, 'base/home.html', context)

def searched_view(request):
    """shows your recipes that correspond to the search query"""
    print(request.POST)
    if request.method == 'POST':
        searched_words = request.POST.get('searched')
     
        search_vectors = SearchVector("recipes", "ingredients", "dish_name", "full_sentence_ingredients" )     
        query = SearchQuery(searched_words)

        recipes = Scraped.objects.annotate(search=search_vectors).filter(search = query)
        context = {'query_recipes': recipes}
        # query = ScrapedRecipes.objects.filter(dish_name__icontains=searched_words)
        # context = {'query_recipes': query }
        return render(request, 'base/search.html', context)
    
def selected_recipe_view(request, pk):
    """carries over informarion of the clicked recipe to the new page"""
    selected_recipe = Scraped.objects.get(pk=pk)
    context = {'selected_recipe': selected_recipe}
    return render(request, 'base/selected_recipe.html', context)

def create_recipe(request):
    """uses forms.py to POST user inputted recipes into database"""
    form = RecipeForm()

    if request.method == 'POST':
        
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/create_recipe.html', context)

