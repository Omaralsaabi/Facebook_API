from django.db import models

# Create your models here.


class FacebookDB(models.Model): 
    username = models.CharField(max_length=100, primary_key=True)
    fid = models.CharField(max_length=100)


