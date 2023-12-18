from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication

from django.contrib.auth import get_user_model
from chats.serializers import UserGetSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser,DjangoModelPermissionsOrAnonReadOnly
from rest_framework import generics,permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import jwt
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from app.tokenauthentication import JWTAuthentication







# Create your views here.




User = get_user_model()
@api_view(['GET'])
# @authentication_classes([TokenAuthentication])  # Add TokenAuthentication
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
# @permission_classes([JWTAuthentication])
def get_user_list(request):
    try:
        # user_obj = User.objects.exclude(id=request.user.id)
        user_obj = User.objects.all()
        print(user_obj)
        serializer = UserGetSerializer(user_obj,many =True)
        return Response(serializer.data,status=200)
    except Exception as e:
        print('Error in getting users list',str(e))
        return Response({'error':'Error is getting users list'},status=400)
    
    
    

        
