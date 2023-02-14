from django.contrib import admin
from .models import Category, Item

# Register your models here.

# on déclare des entités que l'on veut gérer avec le panneau d'administration
# ceci permet d'ajouter, modifier et effacer des enregistrements dans le panneau
# d'administration
admin.site.register(Category)
admin.site.register(Item)