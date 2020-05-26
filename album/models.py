from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

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

	def save(self):
		basewidth = 100
		im = Image.open(self.profile_picture)
		im = im.convert('RGB')
		output = BytesIO()
		wpercentage = (basewidth/float(im.size[0]))
		hsize = int(float(im.size[1]*float(wpercentage)))
		im = im.resize((basewidth,hsize))
		im.save(output, format='JPEG', quality=90)
		output.seek(0)
		self.profile_picture = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.profile_picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		super(Comments, self).save()

class Wish(models.Model):
	name = models.CharField(max_length=100)
	wish = models.TextField()

	def __str__(self):
		return self.wish

class Testimonial(models.Model):
	name = models.CharField(max_length=100)
	testimonial = models.TextField()

	def __str__(self):
		return self.testimonial