from distutils.command.upload import upload
from tkinter import image_names
from django.db import models

class Image(models.Model):
    image_name=models.CharField(max_length=50,unique=True)
    slug=models.CharField(max_length=50,unique=True)
    image=models.ImageField(upload_to='photos/user_images',blank=True)


    def __str__(self):
        return self.image_name