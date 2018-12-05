from rest_framework import permissions

from Employee_Management.apps.common import constant as constant


class IsAdmin(permissions.BasePermission):

    def has_permission(self,request,view):
        if request.user.role == constant.Admin:
            return True
        else:
            return False

class IsHR(permissions.BasePermission):

    def has_permission(self,request,view):
        if request.user.role == constant.HR:
            return True
        else:
            return False

class IsDeveloper(permissions.BasePermission):

    def has_permission(self,request,view):
        if request.user.role == constant.Developer:
            return True
        else:
            return False

