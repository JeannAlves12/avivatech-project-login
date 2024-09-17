from typing import Any
from django import forms
from tela.models import Meeting


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'