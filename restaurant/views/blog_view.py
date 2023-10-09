from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
# Create your views here.


class BlogView(View):
      def get(self, request, *args, **kwargs):

            return render(request, './restaurant.html')
