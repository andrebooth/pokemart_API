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
def pokemart_list(request, format=None):
    #get all the drinks from drink class in models
    #serialize them from serializer class going to take the pokemart list, and to serialize all of them
    #return json

    if request.method == 'GET':
        items = Pokemart.objects.all()
        serializer = PokemartSerialzer(items, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = PokemartSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

#decorator for multiple options GET, PUT, DELETE 
@api_view(['GET', 'PUT', 'DELETE'])

def pokemart_list_detail(request, id, format=None):
#checking to make sure its a valid request (try and except)
    try:
        #for the drink serializer / getting a pokemart item by id, assigning it the pk parameter
        pokemart_id = Pokemart.objects.get(pk=id)
        #if something goes wrong, this exception will be hit
    except Pokemart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #check the different options 
    if request.method == 'GET':
    #bottom 2 lines are all thats needed for get request of an id / moving (return Response(serializer.data) to first GET)
        serializer = PokemartSerialzer(pokemart_id)
        return Response(serializer.data)
   
    #PUT - able to edit the data
    elif request.method == 'PUT':
    #the serializer is grabbing the data for the individual id 
        serializer = PokemartSerialzer(pokemart_id, data=request.data)
        #checking if the request is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        #if its not valid it will throw this error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        #referencing the variable for the pokemart list id and adding the delete method
        pokemart_id.delete()
        #if valid it will return a no content status after deletion
        return Response(status=status.HTTP_204_NO_CONTENT)
        

