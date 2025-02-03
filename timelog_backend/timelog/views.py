from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def hello_world(request):
    return Response(data={'hello': 'world'}, status=status.HTTP_201_OK)
