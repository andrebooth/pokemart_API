#need to inhereit from a model class (line 2)
from email.mime import image
from django.db import models



#creating class that inhereit from Models - how django knows this is a model class 
class Pokemart(models.Model):
#giving the class attributes (name = data type)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
#price will equal the digit value of the item cost for store
    price = models.IntegerField()
#able to upload a photo of an item
    image = models.ImageField(upload_to='uploads/items')

#I will now create a database table from this info, I will create another migration
#I made a migration - the migrations describe the change to the data structure but doesnt apply to the database 
#I need to now migrate (python manage.py migrate, that will apply any unapplied migrations)



#changing the drink object model to be a string instead of object 1 object 2 etc
#need to make sure the indentation is right or it wont be part of the class/function
    def __str__(self):
        return self.name + " " + self.description