from django.db import models

# Create your models here.

class Post(models.Model): # model is a django - create fields library(like android studio)
	title = models.CharField(max_length=120) 
	description = models.TextField()

	def __str__(self): # will show the title of the post in the admin panel
		return self.title 


