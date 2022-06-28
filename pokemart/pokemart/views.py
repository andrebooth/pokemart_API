#this is where we are going to create our endpoints - url where we can access data from
#need to do imports for requests 
from django.http import JsonResponse
from .models import Pokemart
from .serializer import PokemartSerialzer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
#GET: Function that will takr a GET request for all items 
def pokemart_list(request):
    #get all the drinks from drink class in models
    #serialize them from serializer class going to take the pokemart list, and to serialize all of them
    #return json

    if request.method == 'GET':
        items = Pokemart.objects.all()
        serializer = PokemartSerialzer(items, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = PokemartSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
