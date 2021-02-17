from django.urls import path
from .views import MemberListAPIView
urlpatterns=[
    path('', MemberListAPIView.as_view(), name='display')
]