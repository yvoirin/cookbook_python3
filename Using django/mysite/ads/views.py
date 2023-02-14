from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Item

from .forms import ItemForm
from django.http import HttpResponseRedirect

# vue principale comprenant une carte
def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

# vue des enregistrements en JSON pour la carte
# ceci permet de retrouner le résultat d'une requête
# sous la forme d'un service web
def getItems(request):
    resu = []
    if request.method == 'GET':
        # on peut récupérer des paramètres du client web
        search = request.GET['search']
        # on effectue la requête sur la base (avec filter)
        resu = list(Item.objects.values().filter(name__icontains=search))
    
    return JsonResponse({'status': 'ok', 'data': resu}, safe=False)

# on souhaite une vue globale des annonces
def listing(request):
    template = loader.get_template('listing.html')
    # on récupère les annonces classées en ordre
    # chronologique inverse
    results = Item.objects.order_by('-pub_date')
    # on va envoyer le résultat dans la vue
    context = {'results': results}
    return HttpResponse(template.render(context))

# on peut faire une vue pour modifier le contenu de l'annonce
def edit(request, ads_id):
    # on récupère l'annonce dans la base de données
    item = Item.objects.get(id=ads_id)
    # si la vue reçoit un POST, il s'agit donc de la soumission du formulaire
    if request.method == 'POST':
        # on va simplement demander à django de sauvegarder les infos et mettre à jour la base de données
        form = ItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            # on retourne vers l'accueil
            return HttpResponseRedirect('/listing')
    # sinon il s'agit d'un GET, on visualise l'annonce
    else:
        form = ItemForm(instance=item)

    context = {"form": form}
    template = loader.get_template('edit.html')
    # on affichera le formulaire avec les infos de l'annonce
    return HttpResponse(template.render(context, request))

# on peut faire une vue pour ajouter une annonce. Cela ressemble au principe du Edit mais on n'a pas d'annonce à chercher
# dans la base puisqu'il s'agit d'une nouvelle annonce
def add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/listing')
    else:
        form = ItemForm()


    context = {"form": form}
    template = loader.get_template('edit.html')
    return HttpResponse(template.render(context, request))

# on peut prévoir une vue pour effacer une annonce, cela ressemble au principe du Edit ou du Add, sauf
# que l'on utilise la méthode delete de la classe Item. Automatiquement l'annonce sera effacée dans la base de données.
def delete(request, ads_id):
    item = Item.objects.get(id=ads_id)

    if item:
        item.delete()

    return HttpResponseRedirect('/listing')