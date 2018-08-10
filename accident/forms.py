from django import forms
from .models import Accident


class PostForm(forms.Form):
    headline = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'headline', 'placeholder': 'Краткое описание аварии', 'name': 'headline'}))
    text = forms.CharField(widget=forms.Textarea(attrs={
                           'class': 'form-control rounded-0', 'id': 'id_text', 'rows': '3', 'name': 'id_text'}))


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
