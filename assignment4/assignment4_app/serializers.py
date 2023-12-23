from rest_framework import serializers
from .models import book3

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book3
        fields = '__all__'