from rest_framework import serializers
from .models import FileTest

class FileTestSerializer(serializers.ModelSerializer):
    path=serializers.FileField(required=False)

    class Meta:
       model=FileTest
       fields='__all__'
       read_only_fields=('id', )
