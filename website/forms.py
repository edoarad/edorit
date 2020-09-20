from django import forms

class ReceptionForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, initial="Full Name")
    table_name = forms.CharField(label='table_name', max_length=100, initial="Table Name")