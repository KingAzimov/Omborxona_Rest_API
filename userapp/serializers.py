from rest_framework.exceptions import ValidationError
from asosiyapp.models import *
from userapp.models import *
from rest_framework.serializers import ModelSerializer

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','username','password']
#
#     def create(self, validated_data):
#         user = User(
#             username = validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user