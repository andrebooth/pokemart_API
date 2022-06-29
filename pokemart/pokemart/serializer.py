#we will use this serializer to return our model through our API

#need to import rest_framework (thats where its coming from)
from dataclasses import fields
from rest_framework import serializers
#need to import model/pokemart
from .models import Pokemart

#going to describe from a python object to json
class PokemartSerialzer(serializers.ModelSerializer):
#need to have an inner class Meta - Meta data describing the model
    class Meta:
        model = Pokemart
        fields = ['id', 'name', 'description', 'price', 'image']