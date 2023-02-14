from django.db import models

# Create your models here.
class Category(models.Model):
    # colonne name
    name = models.CharField(max_length=200)
    # affichage en texte
    def __str__(self):
        return self.name
class Item(models.Model):
    # colonne name
    name = models.CharField(max_length=200)
    # colonne price
    price = models.FloatField()
    # colonne pub_date
    pub_date = models.DateTimeField()
    # colonne category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # la colonne lon
    lon = models.FloatField()
    # la colonne lat
    lat = models.FloatField()

    # affichage en texte
    def __str__(self):
        return self.name
