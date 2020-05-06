from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.http import HttpResponse
from django.db.models import Q
from .serializers import  TabSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from tabs.models import GuitarTab
from aws.s3Client import s3Client

class TabDetailView(APIView):
    def post(self,request,*args,**kwargs):
        file_serializer = TabSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id =None):
        try:
            tab = GuitarTab.objects.get(id=id)
            tab.delete()
            return HttpResponse(status=204)
        except GuitarTab.DoesNotExist as e:
            return Response({"error": "Given Tab object not found."}, status=404)


class TabListAPIView(generics.ListAPIView):
    serializer_class = TabSerializer
    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        tabs = GuitarTab.objects.all()
        return tabs
