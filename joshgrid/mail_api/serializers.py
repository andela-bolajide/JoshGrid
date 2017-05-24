from django.contrib.auth.models import User, Group

from rest_framework import serializers

from joshgrid.mail_api.models import Mail


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MailSerializer(serializers.ModelSerializer):
    """
    Define Serializer for sending Mails.
    """
    class Meta:
        model = Mail
        fields = ('id', "sender_address", 'receiver_address', 'mail_subject', 'mail_body', 'time_created', 'sent')
