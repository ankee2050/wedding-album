from django import forms
from album.models import Comments, Wish, Testimonial

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ('name','comment','profile_picture',)


class WishForm(forms.ModelForm):

	class Meta:
		model = Wish
		fields = ('name','wish',)

class TestimonialForm(forms.ModelForm):

	class Meta:
		model = Testimonial
		fields = ('name','testimonial',)