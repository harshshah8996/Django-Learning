from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from ..models import UserModel
from ..serializers import UserSerializer


class UserListView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request):

        user_objects = UserModel.objects.all()
        user_ser = UserSerializer(user_objects,many=True)

        return Response({'data':user_ser.data,'message':'List Of Employee'},status=status.HTTP_200_OK)
    

    def post(self,request):
        user_data = request.data
        user_ser = UserSerializer(data=user_data)
        if user_ser.is_valid():
            user_ser.save()
            return Response({'message':'success'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'Error'},status=status.HTTP_406_NOT_ACCEPTABLE)


class UserDetailView(APIView):

    def get(self,request,id):
        pass
    
    def put(self,request,id):
        pass

    def delete(self,request,id):
        pass
    