from django.forms import ModelForm, widgets
from .models import Item

# on peut définir des formulaires si on souhaite faire nos propres formulaires
class ItemForm(ModelForm):
    class Meta:
        # on se base sur la clasee Item
        model = Item
        # on utilise les champs
        fields = ['pub_date', 'name', 'price', 'category', 'lat', 'lon']

        # on peut proposer des outils particuliers pour les champs
        # notamment la saisie d'une date
        widgets = {
            'pub_date': widgets.DateInput(attrs={'type': 'date'})
        }