#this is where we are going to create our endpoints - url where we can access data from
#need to do imports for requests 
from django.http import JsonResponse
from .models import Pokemart
from .serializer import PokemartSerialzer


def pokemart_list(request):
    #get all the drinks from drink class in models
    #serialize them from serializer class going to take the pokemart list, and to serialize all of them
    #return json
   items = Pokemart.objects.all()
   serializer = PokemartSerialzer(items, many=True)
   return JsonResponse(serializer.data, safe=False)