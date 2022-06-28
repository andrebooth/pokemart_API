"""pokemart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # url path for admin
    path('admin/', admin.site.urls),
    # url path to get all the list items in pokemart
    path('pokemart_list/', views.pokemart_list),
    # url path to get individual item by id
    path('pokemart_list/<int:id>', views.pokemart_list_detail)
]

#converting the browser data to json
#need to import format suffix patterns from rest framework url patterns 
urlpatterns = format_suffix_patterns(urlpatterns)