from django.urls import path
from users.views.login_view import LoginView , LogoutView, RegisterView
urlpatterns = [
      
    path('login', LoginView.as_view(), name='login'),
    path('register',RegisterView.as_view(), name='register'),
    path('logout', LoginView.as_view(), name='logout'),

]