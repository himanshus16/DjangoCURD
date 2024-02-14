from django.db import models

class student(models.Model):
    name=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(max_length=50,default='')
    img=models.FileField(upload_to="media")