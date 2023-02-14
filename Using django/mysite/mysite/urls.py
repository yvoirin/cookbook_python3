"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ads import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # vue principale
    path('', views.index, name='index'),
    # mon service web json
    path('getitems/', views.getItems, name='getitems'),
    # la page listing
    path('listing/', views.listing, name='listing'),
    # on va déclarer des urls permettant d'intégrer le ID de l'annonce
    path('item/<ads_id>/edit', views.edit, name="edit"),
    path('item/<ads_id>/delete', views.delete, name="delete"),
    path('item/new', views.add, name="add"),
]
