from django.db import models
#added imports
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Bed(models.Model):
    title = models.CharField(max_length=120)
    size  = models.CharField(max_length=120)
    prices = models.DecimalField(max_digits=100, decimal_places=2)