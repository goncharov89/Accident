from django import forms
from .models import Accident, System, Source


class PostForm(forms.Form):

    headline = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'headline',
            'placeholder': 'Краткое описание аварии',
            'name': 'headline'}))

    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control rounded-0',
            'id': 'id_text',
            'rows': '3',
            'name': 'id_text'}))

    link = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'link',
            'placeholder': 'https://'}))

    link_text = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'link_headline',
            'placeholder': 'SRXXXXX'}))

    system = System.objects.all()
    source = Source.objects.all()
    CHOICES_SYS = [('', 'Выберите систему')]
    CHOICES_SRC = [('', 'Выберите источник')]

    for post in system:
        element = list()
        element.append(post.id)
        element.append(post.name)
        CHOICES_SYS.append(element)

    for post in source:
        element = list()
        element.append(post.id)
        element.append(post.headline)
        CHOICES_SRC.append(element)

    system_id = forms.ChoiceField(choices=CHOICES_SYS, widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'system'}))

    source = forms.ChoiceField(choices=CHOICES_SRC, widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'source'}))


class PostFormEdit(forms.ModelForm):

    class Meta:
        model = Accident
        fields = ('headline', 'text', 'source', 'system',
                  'status', 'causes', 'action', 'fin_effect')

        widgets = {

            'headline': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'headline',
                    'placeholder': 'Краткое описание аварии',
                    'name': 'headline'}),

            'text': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-0',
                    'id': 'id_text',
                    'rows': '3',
                    'name': 'id_text'}),

            'source': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'source'}),

            'system': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'system'}),

            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'status'}),

            'causes': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-0',
                    'id': 'causes',
                    'rows': '3',
                    'placeholder': 'Описание коренной причины'}),

            'action': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-0',
                    'id': 'action',
                    'rows': '3',
                    'placeholder': 'Описание профилактический действий'}),

            'fin_effect': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-0',
                    'id': 'action',
                    'rows': '3',
                    'placeholder': 'Опишите влияние на абонентов/сервис'})}

# Если выбран BPM, отобразить дополнительные поля для модели Tag


class EventForm(forms.Form):

    event_text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control rounded-0',
            'id': 'id_text',
            'rows': '3',
            'name': 'id_text'}))

    link = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'link',
            'placeholder': 'https://'}))

    link_text = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'link_headline',
            'placeholder': 'SRXXXXX'}))


class LinkForm(forms.Form):

    tag_text = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'headline',
            'placeholder': 'Метка',
            'name': 'headline'}))

    link = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'headline',
            'placeholder': 'https://',
            'name': 'headline'}))
