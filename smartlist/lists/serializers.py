from rest_framework import serializers
from lists.models import List

# List Serializer
class ListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'