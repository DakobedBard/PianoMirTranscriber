import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.reverse import reverse as api_reverse
from django.db.models import Q
jwt_payload_handler  = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label="Email Address")
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',

        ]
        extra_kwargs = {"password":{"write_only":True}}
    def validate(self, data):
        return data

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    email= serializers.EmailField(label="Email Address", required=False, allow_blank=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token',
            'id'
        ]
        extra_kwargs = {"password":{"write_only":True}}

    def validate(self, data):

        email = data["email"]
        password = data["password"]
        user = User.objects.filter(email=email).first()
        # If the user object is empty then it will trigger the exception.. not sure of a more elgeant solution this but
        # I'm sure that it exists...
        try:
            passw = user.password
        except Exception as e:
            raise serializers.ValidationError("User with that email address not found")
            return data

        if user.password != password:
             raise serializers.ValidationError("Incorrect Credentials")
        data['id'] = user.id
        return data


