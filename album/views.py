from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import CommentForm, WishForm, TestimonialForm

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
	context = {}
	testimonials = Testimonial.objects.all()
	context['testimonials'] = testimonials
	return render(request, 'album/family.html', context)

def contacts(request):
	return render(request, 'album/contacts.html', {})

def wishes(request):
	context = {}
	wishes = Wish.objects.all()
	context['wishes'] = wishes
	return render(request, 'album/monogram.html', context)

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

def add_wish(request):
	if request.method == 'POST':
		form = WishForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('wishes')
	else:
		form = WishForm()
	return render(request, 'album/add_wish.html',{'form':form})

def add_testimonial(request):
	if request.method == 'POST':
		form = TestimonialForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('family')
	else:
		form = TestimonialForm()
	return render(request, 'album/add_testimonial.html',{'form':form})