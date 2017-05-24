from django.contrib.auth.models import User, Group
from django.http import Http404
from rest_framework import viewsets, status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

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


class MailList(generics.ListCreateAPIView):
    """
    API endpoint that allows Mail to be created or gotten.
    """
    queryset = Mail.objects.all()
    serializer_class = MailSerializer


class MailDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a mail to be retrieved, updated and deleted.
    """
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
