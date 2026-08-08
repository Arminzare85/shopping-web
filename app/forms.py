from django import forms
from django.forms import ModelForm
from app.models import Contact

class contactForm(forms.ModelForm):
    
    class Meta:
            model = Contact
            fields = [
            "name",
            "email",
            "phone",
            "project",
            "subject",
            "message",
        ]


