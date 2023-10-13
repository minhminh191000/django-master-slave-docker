from typing import Any
from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView
from django.views import View
from users.forms.login_form import LoginForm
from users.services.user_services import UserService

class LoginView(TemplateView):
      def __init__(self, **kwargs: Any) -> None:
            super().__init__(**kwargs)
            self.params = {
                  "login_form": LoginForm(),
            }
      def get(self, request, *args, **kwargs):
            return render(request, "./login.html", context=self.params)
      
      def post(self, request, *args, **kwargs):
            auth = UserService(request)
            form = LoginForm(request.POST)
            if form.is_valid():
                  email = form.cleaned_data.get('EMAIL')
                  password = form.cleaned_data.get('PASSWORD')
                  user = auth.login(email, password)
                  if user:
                        result = user.get_info()
                        if result['role'] == 'CONSUMER':
                              return render(request, "./restaurant.html", result)
                        elif result['role'] == 'ADMIN':
                              return HttpResponse("Hello Admin!")
                        else:
                              return HttpResponse('hello con cac!')   
                  else:
                        return HttpResponse("Email or password is wrong !")
            else: 
                  return HttpResponse("Login faid ! Bot suspected.")
            
class LogoutView(TemplateView):
      
      def __init__(self, **kwargs: Any) -> None:
            super().__init__(**kwargs)
      
      def get(self, request, *args, **kwargs):
            auth = UserService(request)
            auth.logout()
            return HttpResponse("Login out")