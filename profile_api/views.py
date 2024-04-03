from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP Method to get, post, patch, put, delete',
            'is similar to traditional view',
            'Gives you the most control over your app logic',
            'is mapped manually to Urls'
        ]

        return Response({'message': 'Hello!' , 'an_apiview': an_apiview})
