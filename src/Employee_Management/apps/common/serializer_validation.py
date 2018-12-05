from rest_framework  import serializers
from django.core.validators import RegexValidator
from rest_framework.validators import UniqueValidator

from Employee_Management.apps.employee.models import UserModel


def char_validator(max_length=None,required=True):
    return serializers.CharField(max_length=max_length,required=required)

def integer_validator(required=True):
    return serializers.IntegerField(required=required)

def email_validator(required=True):
    unique_email_validator = UniqueValidator(queryset=UserModel.objects.all())
    return serializers.EmailField(validators=[unique_email_validator],required=required)

def choices_validator(choices=None,required=True):
    return serializers.ChoiceField(choices= choices , required=required)

def date_validator(required=True):
    return serializers.DateField(required=required)

def mobile_validator(required=True):
    mobile_regex = RegexValidator(regex=r'^[6-9]\d{9}$',message='Please Enter Only 10 Digits - start with 6 to 9')
    return serializers.CharField(validators=[mobile_regex],required=required)