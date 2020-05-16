from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'album/index.html', {})

def wedding(request):
	return render(request, 'album/wedding.html', {})

def album(request):
	return render(request, 'album/album.html', {})

def links(request):
	return render(request, 'album/links.html', {})

def contacts(request):
	return render(request, 'album/contacts.html', {})

def tribute(request):
	return render(request, 'album/tribute.html', {})