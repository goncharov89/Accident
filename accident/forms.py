from django import forms
from .models import Accident


class PostForm(forms.ModelForm):

    class Meta:
        model = Accident
        fields = ('headline', 'text', 'source', 'system')

        help_texts = {
            'headline': 'Краткое описание аварии',
            'text': 'Опишите аварию и ее влияние',

        }


class PostFormEdit(forms.ModelForm):

    class Meta:
        model = Accident
        fields = ('headline', 'text', 'source', 'system', 'status')

# Если выбран BPM, отобразить дополнительные поля для модели Tag


class EventForm(forms.Form):
    event_text = forms.CharField(label="", widget=forms.Textarea)


class LinkForm(forms.Form):
    tag_text = forms.CharField(
        label="Текст", widget=forms.TextInput, required=True)
    link = forms.CharField(
        label="Сслыка", widget=forms.TextInput, required=False)
