from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(('GET',))
def hello_world(request):
    return Response(data={'hello': 'world'}, status=status.HTTP_201_OK)
