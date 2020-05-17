from django import forms
from album.models import Comments

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ('name','comment','profile_picture',)