from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import CommentForm

def index(request):
	return render(request, 'album/index.html', {})

def wedding(request):
	return render(request, 'album/wedding.html', {})

def album(request):
	context = {}
	album_context = Photos.objects.all()
	context['album_dict'] = album_context
	print(context)
	return render(request, 'album/album.html', context)

def family(request):
	return render(request, 'album/family.html', {})

def contacts(request):
	return render(request, 'album/contacts.html', {})

def wishes(request):
	return render(request, 'album/monogram.html', {})

def add_comment_to_photo(request,pk):
	photo = get_object_or_404(Photos, pk=pk)
	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.for_photo = photo
			comment.save()
			return redirect('album')
	else:
		form = CommentForm()

	return render(request, 'album/add_comment.html', {'form':form})