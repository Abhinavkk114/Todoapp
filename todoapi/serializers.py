from rest_framework import serializers
from django.contrib.auth.models import User
from tasks.models import Todos

class UserSerializers(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=['id','username','email','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class TodoSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Todos
        fields='__all__'
    
