from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import UserModel
from ..serializers import UserSerializer
from ..permissions import IsAdmin,IsDeveloper,IsHR
from Employee_Management.apps.common import constant as constant


class UserListView(APIView):

    permission_classes = (IsAdmin|IsHR,)

    def get(self,request):
        
        if request.user.role == constant.Admin:
            user_objects = UserModel.objects.filter()
            user_ser = UserSerializer(user_objects,many=True)

        elif request.user.role == constant.HR:
            user_objects = UserModel.objects.filter(role=constant.Developer)
            user_ser = UserSerializer(user_objects,many=True)

        # elif request.user.role == constant.Developer:
        #     user_object = UserModel.objects.filter(pk=request.user.id).first()
        #     user_ser = UserSerializer(user_object)

        return Response({'data':user_ser.data,'message':'List Of Employees'},status=status.HTTP_200_OK)
    

    def post(self,request):

        if request.user.role == constant.HR and (request.data['role'] == constant.Admin or request.data['role']  == constant.HR ):
            return Response({'message':'You do not have permission to perform this action'},status=status.HTTP_403_FORBIDDEN)

        requesr_data = request.data
        requesr_data['created_by'] = request.user.id
        requesr_data['updated_by'] = request.user.id
        
        user_ser = UserSerializer(data=requesr_data)

        if user_ser.is_valid():
            user_obj = UserModel.objects.create_user(requesr_data)
            user_data = UserSerializer(user_obj).data
            return Response({'message':'Success','data' : user_data },status=status.HTTP_200_OK)
        else:
            return Response({'message':user_ser.errors},status=status.HTTP_406_NOT_ACCEPTABLE)


class UserDetailView(APIView):

    def get(self,request,id):
        
        user_obj = UserModel.objects.filter(pk=id).first()
        if not user_obj:
            return Response({'message':'User is not exist'},status=status.HTTP_406_NOT_ACCEPTABLE)

        if (request.user.role == user_obj.role and request.user.id== id ) or request.user.role == constant.Admin:
            user_data = UserSerializer(user_obj).data
        
        elif request.user.role == constant.HR and user_obj.role == constant.Developer:
            user_data = UserSerializer(user_obj).data
        
        else:
            return Response({'message':'You do not have permission to perform this action'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        return Response({'message':'Success','data' : user_data },status=status.HTTP_200_OK)

    
    def put(self,request,id):

        user_obj = UserModel.objects.filter(pk=id).first()
        if not user_obj:
            return Response({'message':'User is not exist'},status=status.HTTP_406_NOT_ACCEPTABLE)


        if (request.user.role == user_obj.role and request.user.id== id ) or request.user.role == constant.Admin or (request.user.role == constant.HR and user_obj.role == constant.Developer):
            user_ser = UserSerializer(user_obj,data=request.data,partial=True)
        
        else:
            return Response({'message':'You do not have permission to perform this action'},status=status.HTTP_406_NOT_ACCEPTABLE)

        if user_ser.is_valid():
            user_obj = user_obj.update_user(request.data)
            user_data = UserSerializer(user_obj).data
            return Response({'message':'Upated','data' : user_data },status=status.HTTP_200_OK)
        else:
            return Response({'message':user_ser.errors},status=status.HTTP_406_NOT_ACCEPTABLE)


    def delete(self,request,id):
        user_obj = UserModel.objects.filter(pk=id).first()
        if not user_obj:
            return Response({'message':'User is not exist'},status=status.HTTP_406_NOT_ACCEPTABLE)

        if request.user.id == id:
            return Response({'message':'You do not have permission to perform this action'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if request.user.role == constant.Admin or (request.user.role == constant.HR and user_obj.role == constant.Developer):
            user_obj = user_obj.delete_user(request.user.id)
            return Response({'message':'Deleted'},status=status.HTTP_200_OK)
                
        else:
            return Response({'message':'You do not have permission to perform this action'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        