from django.db import models
from django.contrib.postgres.fields import ArrayField

class Scraped(models.Model):
    dish_name = models.TextField(primary_key=True)
    amount = ArrayField(models.TextField(blank=True, null=True)) 
    units = ArrayField(models.TextField(blank=True, null=True))  
    ingredients = ArrayField(models.TextField(blank=True, null=True)) 
    recipes = ArrayField(models.TextField(blank=True, null=True)) 
    dish_img = models.ImageField(null = True, blank= True, upload_to = 'images/')
    full_sentence_ingredients = ArrayField(models.TextField(blank=True, null=True))  

    def __str__(self):
        return self.dish_name
    
    class Meta:
        managed = False
        db_table = 'scraped_recipes'



