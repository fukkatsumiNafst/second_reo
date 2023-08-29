from django import forms
from django.core.exceptions import ValidationError
from .models import Adv

class AdvForms(forms.ModelForm):
    class Meta:
        model = Adv
        fields = ['title', 'description', 'image', 'price', 'auction']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control form-control-lg'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control form-control-lg'}),
            'price' : forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}),
            'auction' : forms.CheckboxInput(artts={'class' : 'form-check-input'}),
            'image' : forms.FileInput(artts={'class' : 'form-control form-control-lg'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('заголовок не может начинаться с вопросительного знака')
        return title

