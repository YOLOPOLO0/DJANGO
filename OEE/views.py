from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    Items = Item.objects.all()
    serializer = ItemSerializer(Items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
