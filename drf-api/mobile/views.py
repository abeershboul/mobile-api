from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import MobileSerializer
# Create your views here.
from .models import Mobile

# Create your views here.
class MobileListView(ListAPIView):
     queryset=Mobile.objects.all()
     serializer_class= MobileSerializer

class MobileDetailView(RetrieveUpdateDestroyAPIView): 
    queryset=Mobile.objects.all()
    serializer_class= MobileSerializer   