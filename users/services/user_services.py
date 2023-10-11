from users.models.user_models import UserModels
from django.contrib.auth import authenticate, login , logout



class UserService():
      
      def __init__(self, request, *args, **kwargs,):
            self.params = {
                  'request': request,
            }
      
      def login(self, username, password):
            user = authenticate(username=username, password=password)
            if user is not None:
                  login(self.params['request'], user=user)
                  return True
            else:
                  return False
      
      def logout(self):
            logout(self.params['request'])
            return True