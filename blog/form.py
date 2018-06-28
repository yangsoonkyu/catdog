from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = (
            'type',
            'gender',
            'age',
            'find_point',
            'find_date',
            'find_time',
            'other',
            'animal_shelter',
            'shelter_tel',
        )
