from django.db import models
from django import forms

# Create your models here.
class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    publisher = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title
        
    def get_fields(self):
    # make a list of field/values.
        return [(field.name, field.value_to_string(self)) for field in Book._meta.fields]