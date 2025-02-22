from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from timelog.serializers import CheckSerializer

from .models import CheckIn

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
        print(err)
        return Response(
            data={'error': 'Hubo un error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('POST',))
@permission_classes([AllowAny])
def login(request):
    try:
        usr = request.data['email']
        pss = request.data['password']
        user = User.objects.get(username=usr, password=pss)
        if user:
            token = Token.objects.get_or_create(user=user)[0]
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


@api_view(('POST',))
@permission_classes([IsAuthenticated])
def check(request):
    try:
        user = User.objects.get(username=request.user)
        body = request.data.copy()
        print(type(request.data))
        body['user'] = user.id
        serializer = CheckSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'not found'},
                            status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response(
            data={'error': 'hubo un error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def getAll(request):
    print(request)
    serializer = CheckSerializer(CheckIn.objects.all(), many=True)
    print(serializer)
    return Response(data={'hello': 'world'}, status=status.HTTP_200_OK)
