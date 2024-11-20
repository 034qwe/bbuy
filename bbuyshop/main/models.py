from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField('name',max_length=100),
    inside = models.ManyToManyField('ingredient',)



class Ingredient(models.Model):
    how_much = models.IntegerField()
    name_ing = models.CharField(max_length=300)