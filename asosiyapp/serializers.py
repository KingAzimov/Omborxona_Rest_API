from rest_framework.exceptions import ValidationError
from .models import *
from rest_framework.serializers import ModelSerializer

class MijozSerializer(ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'

    def validate_qarz(self, qiymat):
        if qiymat > 50000:
            raise ValidationError("Buncha qarz bo'lishi mumkin emas")
        return qiymat

class MahsulotSerializer(ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']

    def create(self, validated_data):
        user = User(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user