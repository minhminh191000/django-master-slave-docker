from django.urls import path
from users.views.login_view import LoginView
urlpatterns = [
      
    path('login', LoginView.as_view(), name='login'),

]