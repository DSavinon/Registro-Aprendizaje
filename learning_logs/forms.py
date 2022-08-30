from dataclasses import fields
from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": "Entry:"}
        # usamos widget para cambiar el formato del campo de texto, le damos 80 columnas al area de texto
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
