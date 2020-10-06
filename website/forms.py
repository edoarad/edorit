from django import forms

from . import models

TABLES_NAMES = [
    "Edo's Family", 
    "Orit's Family", 
    "Arazim", 
    "Edo's Highschool",
    "Orit's Highschool",
    "Edo's Kindergarden",
    "Orit's Kidergarden",
]
TABLE_CHOICES = [(name, name) for name in TABLES_NAMES]

def validate_name_no_dup(guest_name):
    if models.Guest.objects.filter(name=guest_name):
        print(f"Name collision found for {guest_name}")
        raise forms.ValidationError("Name already taken!")

class ReceptionForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={"placeholder": "Full Name", "class": "form-control mb-2 mr-sm-2"}),
                            validators=[validate_name_no_dup])
    table_name = forms.ChoiceField(label='Table Name', widget=forms.RadioSelect, choices=TABLE_CHOICES)