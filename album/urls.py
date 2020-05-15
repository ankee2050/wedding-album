from django.urls import path
from .views import *

urlpatterns = [
	path('',index, name='index'),
	path('wedding', wedding, name='wedding'),
	path('album', album, name='album'),
	path('links', links, name='links'),
	path('contacts', contacts, name='contacts'),
]