from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import FileTestSerializer
from .models import FileTest
# Create your views here.
class FileTestViewSet(ModelViewSet):
    queryset=FileTest.objects.all()
    serializer_class = FileTestSerializer

    def create(self, request, *args, **kwargs):
        return super(FileTestViewSet, self).create(request, *args, **kwargs)
