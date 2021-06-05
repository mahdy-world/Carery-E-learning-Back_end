from django import forms
from django.db.models import fields
from .models import Review , RATE_CHOISES



class RateForm (forms.ModelForm):
    
    class Meta:
        model = Review
        fields= ("text" , "rate")
        