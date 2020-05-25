from django.db import models
from django.contrib.auth.models import User

cities = [
    ( 'BGL','Bangalore'),
    ('DEL','Delhi'),
    ('BOM','Mumbai'),
    ('NE','North-East'),
    ('CHD', 'Chandigarh'),
    ('PJB', 'Punjab'),
    ('AMD', 'Ahemdabad'),
    ('OT', 'Others')
]

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    mobile = models.CharField(max_length = 11)
    age = models.IntegerField(default = 15)
    description = models.CharField(max_length = 1000, null = True)
    cityPreference = models.CharField(max_length = 30, choices = cities)
