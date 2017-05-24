from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

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


@csrf_exempt
def mail_list(request):
    """
    List all mails, or create a new mail.
    """
    if request.method == 'GET':
        mail = Mail.objects.all()
        serializer = MailSerializer(mail, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def mail_detail(request, pk):
    """
    Retrieve, update or delete a mail.
    """
    try:
        mail = Mail.objects.get(pk=pk)
    except Mail.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MailSerializer(mail)
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MailSerializer(mail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mail.delete()
        return HttpResponse(status=204)
