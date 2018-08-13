from django import forms
from .models import Accident, System, Source


class PostForm(forms.Form):
    headline = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'headline', 'placeholder': 'Краткое описание аварии', 'name': 'headline'}))
    text = forms.CharField(widget=forms.Textarea(attrs={
                           'class': 'form-control rounded-0', 'id': 'id_text', 'rows': '3', 'name': 'id_text'}))
    link = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'headline', 'placeholder': 'https://'}))
    link_text = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'headline', 'placeholder': 'SRXXXXX'}))

    system = System.objects.all()
    source = Source.objects.all()
    CHOICES_sys = [('', 'Выберите систему')]
    CHOICES_src = [('', 'Выберите источник')]

    for post in system:
        element = list()
        element.append(post.id)
        element.append(post.name)
        CHOICES_sys.append(element)

    for post in source:
        element = list()
        element.append(post.id)
        element.append(post.headline)
        CHOICES_src.append(element)

    system_id = forms.ChoiceField(choices=CHOICES_sys, widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'source'}))
    source = forms.ChoiceField(choices=CHOICES_src, widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'source'}))


class PostFormEdit(forms.ModelForm):

    class Meta:
        model = Accident
        fields = ('headline', 'text', 'source', 'system', 'status')

# Если выбран BPM, отобразить дополнительные поля для модели Tag


class EventForm(forms.Form):

    event_text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control rounded-0', 'id': 'id_text', 'rows': '3', 'name': 'id_text'}))


class LinkForm(forms.Form):

    tag_text = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'headline', 'placeholder': 'Метка', 'name': 'headline'}))
    link = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'headline', 'placeholder': 'https://', 'name': 'headline'}))
