from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets


#2 class pertama belajar tentang APIView dan ViewSet
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP Method to get, post, patch, put, delete',
            'is similar to traditional view',
            'Gives you the most control over your app logic',
            'is mapped manually to Urls'
        ]

        return Response({'message': 'Hello!' , 'an_apiview': an_apiview})

    def post(self, request):
        """Create Hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test viewset API"""
    serializer_class= serializers.HelloSerializer #diambil dari class Helloserializer pada file serializers.py 

    def list(self,request):
        a_viewset = [
            'viewset action terdiri dari (list, create, retrieve, update, partial_update)',
            'secara automatis mapping urls pake routers',
            'sedikit code dengan banyak fungsionalitas'
        ]                   
        return Response({
            'message' : 'Hello',
            'a_viewset' : a_viewset
        })

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data) #cara ngedapetin data dari request oleh user
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Hanlde getting an object by its ID"""
        return Response ({'http_method':'GET'})

    def update(self, request, pk=None):
        """Hanlde update an object"""
        return Response ({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Hanlde update part an object """
        return Response ({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Hanlde update part an object """
        return Response ({'http_method':'DELETE'})



