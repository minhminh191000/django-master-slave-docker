from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView
from django.views import View
# Create your views here.
from users.forms.login_form import LoginForm


class LoginView(TemplateView):
      def __init__(self):
            self.params = {
                  # "AccountCreate": False,
                  "login_form": LoginForm(),
            }
      def get(self, request, *args, **kwargs):
            return render(request, "./login.html", context=self.params)
      
      def post(self, request, *args, **kwargs):
            form = LoginForm(request.POST)
            if form.is_valid(): 
                  return HttpResponse("Yay! you are human.") 
            else: 
                  return HttpResponse("OOPS! Bot suspected.")