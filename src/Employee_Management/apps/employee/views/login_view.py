from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

import requests,json

class LoginView(APIView):

    permission_classes = (AllowAny,)

    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user_obj = authenticate(email=email,password=password)

        if user_obj:
            payload = {
                'email' : email,
                'password':password
            }
            
            jwt_response = requests.post('http://localhost:7000/api-token-auth/',data=payload)
            response = json.loads(jwt_response.text)
            return Response({'data':response['token'],'message':('Welcome ' + str(user_obj.first_name))},status=status.HTTP_200_OK)
        
        else:
            return Response({'message':'Please Enter Valid Email & Password'},status=status.HTTP_406_NOT_ACCEPTABLE)