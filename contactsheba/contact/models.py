from django.db import models


class ContactModel (models.Model):
    user_id=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.IntegerField()
    