from django.forms import ModelForm, widgets
from contact.models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    FullName = forms.CharField(required=True, max_length=50, label='Full Name')
    Email = forms.CharField(required=True, max_length=256, label='Email Address')
    class Meta:
        model = Contact
        fields = ['FullName', 'Email', 'Queries']

    widgets = {
        'FullName':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Full Name'}),
        'Email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email Address'}),
    }