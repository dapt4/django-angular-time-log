from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# Create your views here.


@api_view(('POST',))
@permission_classes([AllowAny])
def register(request):
    try:
        usr = request.data['email']
        pss = request.data['password']
        user = User(username=usr, password=pss, email=usr)
        user.save()
        return Response(data={'message': 'done'}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response(
            data={'error': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('POST',))
@permission_classes([AllowAny])
def login(request):
    try:
        usr = request.data['email']
        pss = request.data['password']
        user = User.objects.get(username=usr, password=pss)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'token': token.key},
                            status=status.HTTP_200_OK)
        else:
            return Response(
                data={'error': "username and password don't match"},
                status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response(
            data={'error': 'hubo un error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def hello_world(request):
    return Response(data={'hello': 'world'}, status=status.HTTP_200_OK)
