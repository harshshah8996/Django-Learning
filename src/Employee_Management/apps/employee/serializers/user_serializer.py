from rest_framework import serializers

from ..models import UserModel
from Employee_Management.apps.common import serializer_validation as validator
from Employee_Management.apps.common import constant as constant

class UserSerializer(serializers.ModelSerializer):
    
    first_name = validator.char_validator(max_length=100)
    last_name = validator.char_validator(max_length=100)
    gender = validator.choices_validator(choices=constant.GENDER_CHOICES)
    dob = validator.date_validator()
    email = validator.email_validator()
    role = validator.choices_validator(choices=constant.ROLE_CHOICES)
    password = validator.char_validator(max_length=50)
    mobile_no = validator.mobile_validator()
    
    class Meta:
        model = UserModel
        fields = '__all__'
    
