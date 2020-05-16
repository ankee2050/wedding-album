from django.urls import path
from .views import *

urlpatterns = [
	path('',index, name='index'),
	path('wedding', wedding, name='wedding'),
	path('album', album, name='album'),
	path('family', family, name='family'),
	path('contacts', contacts, name='contacts'),
	path('wishes', wishes, name='wishes'),
]