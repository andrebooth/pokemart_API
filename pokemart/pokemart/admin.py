#where we can register the different tables we want to show up in our admin panel

from django.contrib import admin
from .models import Pokemart

admin.site.register(Pokemart)