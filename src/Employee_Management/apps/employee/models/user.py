from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.utils import timezone

from Employee_Management.apps.common import constant as constant


class UserManager(BaseUserManager):

    def create_user(self,user_data):
        user = self.model(
            first_name = user_data.get('first_name'),
            last_name = user_data.get('last_name'),
            gender = user_data.get('gender'),
            dob = user_data.get('dob'),
            email = user_data.get('email'),
            role = user_data.get('role'),
            mobile_no = user_data.get('mobile_no'),
            password = user_data.get('password'),
            created_by = user_data.get('created_by'),
            updated_by = user_data.get('updated_by'),
        )

        user.set_password(user.password)
        user.save(using=self._db)
        return user


    # def get_queryset(self):
    #     return super(UserManager, self).get_queryset().filter(is_deleted=False)
    #     return self.get_queryset().filter(is_delete=False)


class UserModel(AbstractBaseUser):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=constant.GENDER_CHOICES,max_length=1)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    role = models.CharField(choices=constant.ROLE_CHOICES,max_length=50)
    password = models.CharField(max_length=250)

    mobile_validator = RegexValidator(regex=r'^[6-9]\d{9}$',message='Enter Valid Mobile Number')
    mobile_no = models.CharField(validators=[mobile_validator],max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(default=None,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default=None,null=True)

    is_delete = models.IntegerField(default=0)
    deleted_at = models.DateTimeField(default=None,null=True)
    deleted_by = models.IntegerField(default=None,null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.first_name
    

    def update_user(self,user_data):

        self.first_name = user_data.get('first_name')
        self.last_name = user_data.get('last_name')
        self.gender = user_data.get('gender')
        self.dob = user_data.get('dob')
        self.email = user_data.get('email')
        self.role = user_data.get('role')
        self.mobile_no = user_data.get('mobile_no')

        self.save()
        return self


    def delete_user(self,user_master):
        self.is_delete = True
        self.deleted_at = timezone.now()
        self.deleted_by = user_master

        self.save()
        return self