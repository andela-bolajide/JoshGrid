"""Define views for the API."""

from django.contrib.auth.models import User, Group
from rest_framework import generics, viewsets, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from joshgrid.mail_api.models import Mail
from joshgrid.mail_api.permissions import IsOwnerOrReadOnly
from joshgrid.mail_api.serializers import (
    UserSerializer, GroupSerializer, MailSerializer
)

from .mail import local_send_email

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    """Create entry point for the root of the API."""
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('mail-list', request=request, format=format)
    })


class MailHighlight(generics.GenericAPIView):
    """Define Mail Highlight class."""

    queryset = Mail.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        """Define function to get highlighted mails."""
        mail = self.get_object()
        return Response(mail.highlighted)


class UserList(generics.ListAPIView):
    """API endpoint that allows users to be viewed."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MailList(generics.ListCreateAPIView):
    """API endpoint that allows Mail to be created or gotten."""

    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """Override inbuilt function to associate mails with users."""
        print('#'*50)
        print(self.request.POST)
        print('#'*50)
        local_send_email(self.request)
        serializer.save(sender=self.request.user)


class MailDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows a mail to be retrieved, updated and deleted."""

    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
