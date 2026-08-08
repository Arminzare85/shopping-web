from django.db import models

# Create your models here.
from django import forms
from django.forms import ModelForm


class Contact(models.Model):
    name = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    