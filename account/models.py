from django.db import models
from django.contrib.auth.models import User

cities = [
    ('Bangalore', 'BGL'),
    ('Delhi','DEL'),
    ('Mumbai', 'BOM'),
    ('North-East', 'NE'),
]

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    mobile = models.IntegerField()
    age = models.IntegerField(default = 15)
    description = models.CharField(max_length = 1000, null = True)
    cityPreference = models.CharField(max_length = 30, choices = cities)
