from django import forms #import ModelForm, CharField
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from users.models.user_models import UserModels
# from captcha.fields import ReCaptchaField 
# from captcha.widgets import ReCaptchaV2Checkbox

class RegisterForm(forms.ModelForm):
      EMAIL = forms.EmailField(widget=forms.EmailInput(), label='Email', required=True)
      FULL_NAME = forms.CharField(widget=forms.TextInput(), label='Full Name', required=True)
      PHONE_NUMBER = forms.CharField(widget=forms.TextInput(), label='Phone Number', required=True)
      BIRTH_DAY = forms.DateField(widget=forms.DateInput(), label="Birth Day", required=True)
      PASSWORD = forms.CharField(widget=forms.PasswordInput(), label="Password", required=True)
      PASSWORD2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password", required=True)
      # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 
      
      class Meta():
            model = UserModels
            fields = ('EMAIL', 'FULL_NAME', 'PHONE_NUMBER', 'BIRTH_DAY','PASSWORD',)

      def clean(self):
            cleaned_data = super(RegisterForm, self).clean()
            password = cleaned_data.get("PASSWORD")
            confirm_password = cleaned_data.get("PASSWORD2")

            if password != confirm_password:
                  raise forms.ValidationError(
                        "password and confirm_password does not match"
                  )



