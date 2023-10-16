from users.models.user_models import UserModels, CHOICES_ROLE
from django.contrib.auth import authenticate, login , logout
from typing import Mapping, Any, Dict


class UserService():
      
      def __init__(self, request, *args, **kwargs,):
            self.params = {
                  'request': request,
            }
            
      
      def login(self, email, password):
            user = authenticate(self.params['request'], email=email, password=password)
            if user is not None:
                  login(self.params['request'], user=user)
                  user_data = UserModels.objects.get(email=email)
                  return user_data
            else:
                  return False
      
      def register(self, user: Dict[str, Any], password, **kwargs):
            try:
                  new_user = UserModels.objects.create(user)
                  return True, new_user.id
            except Exception as e:
                  return False, str(e)
                  


      def logout(self):
            logout(self.params['request'])
            return True