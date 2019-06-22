from captcha.fields import CaptchaField
from django import forms


class RegisterForm(forms.Form):
    user = forms.CharField()
    passwd = forms.CharField()
    captcha = CaptchaField()