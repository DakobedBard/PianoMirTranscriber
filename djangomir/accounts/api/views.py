from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_jwt.settings import api_settings
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.filters import (SearchFilter, OrderingFilter)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from accounts.api.serializers import UserLoginSerializer, UserCreateSerializer

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from .permissions import AnonPermissionOnly

User = get_user_model()


User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER
from rest_framework_jwt.serializers import JSONWebTokenSerializer
class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'email'

    def validate(self, attrs):

        password = attrs.get("password")
        user_obj = User.objects.filter(email=attrs.get("email")).first() or User.objects.filter(username=attrs.get("email")).first()
        if user_obj is not None:
            credentials = {
                'username':user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = _('User account is disabled.')
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg)

            else:
                msg = _('Must include "{username_field}" and "password".')
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = _('Account with this email/username does not exists')
            raise serializers.ValidationError(msg)




class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserCreateSerializer
        if serializer.validate("",data):
            user = User(username = data['username'], email=data['email'], password =data['password'])
            user.save()
            return Response(data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

from rest_framework import generics, mixins
class UserLoginView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserLoginSerializer
    def get(self, request, *args, **kwargs):
        username = self.request.query_params.get('username', None)
        username = username.split("/")[0]
        userID = User.objects.only('id').get(username=username).id
        return Response({'userid':userID}, status=HTTP_200_OK)




