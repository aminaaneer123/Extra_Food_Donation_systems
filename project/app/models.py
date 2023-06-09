from django.db import models



from django.db import models


# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Email=models.CharField(max_length=10)
    Password=models.CharField(max_length=20)