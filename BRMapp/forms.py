from django import forms

class NewBookForm(forms.Form):
    # forms is a module(python file).
    # Form(parent class) is a class in module forms. 

    title = forms.CharField(label='Title',max_length=100)
    price = forms.FloatField(label='Price')
    author = forms.CharField(label='Author')
    publisher = forms.CharField(label='publisher')

class SearchForm(forms.Form):
    title = forms.CharField(label='Title',max_length=100)

