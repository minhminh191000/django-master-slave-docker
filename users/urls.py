from django.urls import path
from users.views.login_view import LoginView , LogoutView
urlpatterns = [
      
    path('login', LoginView.as_view(), name='login'),
    path('logout', LoginView.as_view(), name='logout'),

]