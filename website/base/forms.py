from django import forms
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=255)
    email = forms.EmailField(label=_('Email'))
    message = forms.CharField(label=_('Message'), widget=forms.Textarea(attrs={"rows": 9}))
    captcha = CaptchaField(label=_('Captcha'))
