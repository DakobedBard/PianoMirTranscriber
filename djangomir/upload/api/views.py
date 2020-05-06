from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.http import HttpResponse
from django.db.models import Q
from upload.models import DocumentFile
from .serializers import  DocumentFileSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
User = get_user_model()
from aws.s3Client import s3Client

class DocumentFileDetailView(APIView):

    def get(self,request, id = None):
        instance = self.get_object
    def post(self,request,*args,**kwargs):
        file_serializer = DocumentFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id =None):
        try:
            doc = DocumentFile.objects.get(id=id)
            doc.delete()
            return HttpResponse(status=204)
        except DocumentFile.DoesNotExist as e:
            return Response({"error": "Given question object not found."}, status=404)
        print("innstance" + doc.name)

class DocumentListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = DocumentFileSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        qs = DocumentFile.objects.all()
        query = self.request.GET.get("q")
        userID = self.request.query_params.get('id', None)
        if query is not None:
            qs = qs.filter(Q(title__icontains=query))
        return qs
