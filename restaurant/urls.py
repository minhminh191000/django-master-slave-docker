from django.urls import path
from restaurant.views.blog_view import BlogView

urlpatterns = [
    # ユーザー
    path('', BlogView.as_view(), name='blog'),

]