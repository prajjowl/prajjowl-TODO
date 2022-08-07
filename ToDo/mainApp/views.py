from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
#CRUD operations
class ListTodo(generics.ListAPIView): #Read
    queryset=ToDo.objects.all()
    serializer_class=ToDoserializer

class DetailTodo(generics.RetrieveUpdateAPIView): #Update
    queryset=ToDo.objects.all()
    serializer_class=ToDoserializer  

class CreateTodo(generics.CreateAPIView): #Create
    queryset=ToDo.objects.all()
    serializer_class=ToDoserializer 

class DeleteTodo(generics.DestroyAPIView): #Delete
    queryset=ToDo.objects.all()
    serializer_class=ToDoserializer   
