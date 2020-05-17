from django.db import models

class Photos(models.Model):
	photo_name = models.CharField(max_length=100)
	thumb_name = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.photo_name

class Comments(models.Model):
	name = models.CharField(max_length=100)
	comment = models.TextField()
	for_photo = models.ForeignKey(Photos, on_delete=models.CASCADE)
	profile_picture = models.ImageField(upload_to='profile_pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name