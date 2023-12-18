from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer,LoginSerializer
from rest_framework import status
from app.tokenauthentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
 
# Create your views here.

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201,content_type='application/json')
    return Response(serializer.errors,status=400,content_type='application/json')

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        token = JWTAuthentication.generate_token(payload=serializer.data)
       
        return  Response({
            "message":"Login Succesfull",
            'token':token,
            "user":serializer.data
        },status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# User = get_user_model()
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_user_list(request):
#     print('User permissions:', request.user.get_all_permissions())
#     print(request.user.get_all_permissions())
#     print('User permissions:', request.user.get_all_permissions())
#     try:
#         user_obj = User.objects.exclude(id=request.user.id)
#         print(user_obj)
#         serializer = UserGetSerializer(user_obj,many =True)
#         return Response(serializer.data,status=200)
#     except Exception as e:
#         print('Error in getting users list',str(e))
#         return Response({'error':'Error is getting users list'},status=400)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated

# from .models import User  # Make sure to import your User model
# from .serializers import UserGetSerializer  # Import your serializer

# class UserListView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         try:
#             # Exclude the currently authenticated user
#             user_obj = User.objects.exclude(id=request.user.id)

#             # Serialize the queryset
#             serializer = UserGetSerializer(user_obj, many=True)

#             # Return the serialized data in the response
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             # Handle exceptions and return an error response
#             print('Error in getting users list', str(e))
#             return Response({'error': 'Error in getting users list'}, status=status.HTTP_400_BAD_REQUEST)
