from .models import Membership
from .serializers import MembershipListSerializer
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView, 
    CreateAPIView, 
    RetrieveUpdateAPIView
    )

class MemberListAPIView(ListAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipListSerializer