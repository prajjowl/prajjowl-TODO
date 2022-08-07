from rest_framework import serializers
from .models import *

class ToDoserializer(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        field=('id','Title','Description','Date','Completed')