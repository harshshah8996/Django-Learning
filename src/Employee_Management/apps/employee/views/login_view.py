from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate

from ..models import UserModel
from ..serializers import UserSerializer

import requests,json

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


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
            
            # default JWT implementation
            # jwt_response = requests.post('http://localhost:7000/api-token-auth/',data=payload)
            # response = json.loads(jwt_response.text)
            # token = response['token']

            # manually JWT generation

            payload = jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)

            return Response({'data':token,'message':('Welcome ' + str(user_obj.first_name))},status=status.HTTP_200_OK)
        
        else:
            return Response({'message':'Please Enter Valid Email & Password'},status=status.HTTP_406_NOT_ACCEPTABLE)