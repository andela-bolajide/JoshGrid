from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from joshgrid.mail_api.models import Mail
from joshgrid.mail_api.serializers import UserSerializer, GroupSerializer, MailSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET', 'POST'])
def mail_list(request):
    """
    List all mails, or create a new mail.
    """
    if request.method == 'GET':
        mail = Mail.objects.all()
        serializer = MailSerializer(mail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def mail_detail(request, pk):
    """
    Retrieve, update or delete a mail.
    """
    try:
        mail = Mail.objects.get(pk=pk)
    except Mail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MailSerializer(mail)
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        serializer = MailSerializer(mail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
