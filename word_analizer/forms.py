from django import forms

from .models import Text

import word_analizer.services as services


class TextForm(forms.ModelForm):

    text = forms.CharField(
        widget=forms.Textarea(attrs={"rows": "5", "class": "form-control"})
    )

    class Meta:
        model = Text
        fields = ("text",)