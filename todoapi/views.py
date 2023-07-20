from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication,permissions

from todoapi.serializers import UserSerializers,TodoSerializer
from tasks.models import Todos

class UserView(ModelViewSet):
    model=User
    serializer_class=UserSerializers
    queryset=User.objects.all()

    # def create(self, request, *args, **kwargs):
    #     serializer=UserSerializers(data=request.data)
    #     if serializer.is_valid():
    #         usr=User.objects.create_user(**serializer.data)
    #         serializer=UserSerializers(usr)
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)

class TodoView(ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todos.objects.all()
    # authentication_classes=[authentication.BasicAuthentication]/
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)
    
    # def list(self,request,*args,**kwargs):
    #     qs=Todos.objects.filter(usr=request.user)
    #     serializer=TodoSerializer(qs,many=True)
    #     return Response(data=serializer.data)

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)

