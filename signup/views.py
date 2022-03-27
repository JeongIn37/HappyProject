from django.shortcuts import render

from django.core import cache
from rest_framework import status,  generics  # generics class-based view 사용할 계획
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
from .models import User

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer # serialize 대상 정의
    permission_classes = (AllowAny,) # 접근 허용 범위

    def post(self, request):
        serializer = self.serializer_class(data=request.data) # serialize를 통해 인스턴스로 만들어줌
        serializer.is_valid(raise_exception=True) # validation 수행
        serializer.save() # serialize 내 create() 실행
        status_code = status.HTTP_201_CREATED # 생성 성공
        response = {
            'success': "True",
            'status code': status_code,
            'message': "user registered successfully!",
        }
        return Response(response, status=status_code)

class UserLoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,) #모든 사용자 접근가능
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        user = serializer.validated_data
        if user['id'] == "None":
            return Response({"message": "fail"}, status=status.HTTP_401_UNAUTHORIZED)

        status_code = status.HTTP_200_OK 
        return Response(
            {
                 "id": UserSerializer(
                     user,context=self.get_serializer_context()
                 ).data.get('id'),
                 'success': "True",
                 "status_code": status_code,
                 "message": "Login success!",
            }
        ) 