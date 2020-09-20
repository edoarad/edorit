from django import forms

class ReceptionForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={"placeholder": "Full Name", "class": "form-control mb-2 mr-sm-2"}))
    table_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={"placeholder": "Table Name", "class": "form-control mb-2 mr-sm-2"}))