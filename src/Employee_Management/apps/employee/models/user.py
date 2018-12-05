from django.db import models
from django.core.validators import RegexValidator
from Employee_Management.apps.common import constant as constant

class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=constant.GENDER_CHOICES,max_length=1)
    dob = models.DateField()
    email = models.EmailField()
    role = models.CharField(choices=constant.ROLE_CHOICES,max_length=50)

    mobile_validator = RegexValidator(regex=r'^[6-9]\d{9}$',message='Enter Valid Mobile Number')
    mobile_no = models.CharField(validators=[mobile_validator],max_length=10)

    class Meta:
        db_table = 'user'
    