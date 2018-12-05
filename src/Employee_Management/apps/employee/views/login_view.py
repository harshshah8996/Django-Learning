from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class LoginView(APIView):

    permission_classes = (AllowAny,)

    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user_obj = authenticate(email=email,password=password)

        if user_obj:
            return Response({'message':('Hello , %s',user_obj.first_name)},status=status.HTTP_200_OK)
        else:
            return Response({'message':'Please Enter Valid Email & Password'},status=status.HTTP_406_NOT_ACCEPTABLE)