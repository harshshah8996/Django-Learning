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

        user_ser = UserSerializer(data=request.data)

        if user_ser.is_valid():
            user_obj = UserModel.objects.create_user(request.data)
            user_data = UserSerializer(user_obj).data
            return Response({'message':'Success','data' : user_data },status=status.HTTP_200_OK)
        else:
            return Response({'message':user_ser.errors},status=status.HTTP_406_NOT_ACCEPTABLE)


class UserDetailView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request,id):

        user_obj = UserModel.objects.filter(pk=id).first()
        if not user_obj:
            return Response({'message':'User is not exist'},status=status.HTTP_406_NOT_ACCEPTABLE)

        user_data = UserSerializer(user_obj).data
        return Response({'message':'Success','data' : user_data },status=status.HTTP_200_OK)

    
    def put(self,request,id):

        user_obj = UserModel.objects.filter(pk=id).first()
        if not user_obj:
            return Response({'message':'User is not exist'},status=status.HTTP_406_NOT_ACCEPTABLE)

        user_ser = UserSerializer(user_obj,data=request.data)

        if user_ser.is_valid():
            user_obj = UserModel.objects.update_user(user_obj,request.data)
            user_data = UserSerializer(user_obj).data
            return Response({'message':'Upated','data' : user_data },status=status.HTTP_200_OK)
        else:
            return Response({'message':user_ser.errors},status=status.HTTP_406_NOT_ACCEPTABLE)


    def delete(self,request,id):
        user_obj = UserModel.objects.filter(pk=id).first()
        if not user_obj:
            return Response({'message':'User is not exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        # delete_by = request.user.id
        delete_by = None
        user_obj = UserModel.objects.delete_user(user_obj,delete_by)

        return Response({'message':'Deleted'},status=status.HTTP_200_OK)