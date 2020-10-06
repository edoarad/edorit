from django import forms

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

class ReceptionForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={"placeholder": "Full Name", "class": "form-control mb-2 mr-sm-2"}))
    table_name = forms.ChoiceField(label='Table Name', widget=forms.RadioSelect, choices=TABLE_CHOICES)