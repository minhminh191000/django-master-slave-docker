from django import forms #import ModelForm, CharField
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from users.models.user_models import UserModels
# from captcha.fields import ReCaptchaField 
# from captcha.widgets import ReCaptchaV2Checkbox

class LoginForm(forms.ModelForm):
      EMAIL = forms.EmailField(widget=forms.EmailInput(), label='Email', required=True)
      PASSWORD = forms.CharField(widget=forms.PasswordInput(), label="Password", required=True)
      # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 
      
      class Meta():
            model = UserModels
            fields = ('EMAIL', 'PASSWORD',)

      # def save(self, commit=True):
      #       user = super().save(commit=False)
      #       # user.set_password(self.cleaned_data["password"])
      #       # if commit:
      #             # user.save()
      #       return user


