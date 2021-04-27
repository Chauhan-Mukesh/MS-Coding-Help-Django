from django import forms
from django.core import validators

from .models import *


class CommentOnPost(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class ContactUs(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message']
