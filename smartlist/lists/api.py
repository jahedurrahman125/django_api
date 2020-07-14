from lists.models import List
from rest_framework import viewsets, permissions
from .serializers import ListSerialiser

# List Viewset
class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ListSerialiser

 
