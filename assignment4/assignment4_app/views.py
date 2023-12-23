from django.shortcuts import render
from .models import book3
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

#this will list all the books and we can also add one
class books_list_create(ListCreateAPIView):
    queryset = book3.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

#Retrieve, Update and delete 
class books_RUD(RetrieveUpdateDestroyAPIView):
    queryset = book3.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
