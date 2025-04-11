from django import forms
from .models import *

class Booksform(forms.ModelForm):
    no = forms.IntegerField(label='Book Id')
    name = forms.CharField(label='Book Name',max_length=30)
    author = forms.CharField(label='Author Name',max_length=40)
    edition = forms.CharField(label='Book Edition')
    price = forms.FloatField(label='Book Price')

    class Meta:
        model = library
        fields = '__all__'

class searchbookform(forms.Form):
    bno = forms.IntegerField()

class deleteform(forms.Form):
    bno = forms.IntegerField()