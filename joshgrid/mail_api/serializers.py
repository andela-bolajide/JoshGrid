"""Define serializer for models."""

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from joshgrid.mail_api.models import Mail


class UserSerializer(serializers.ModelSerializer):
    """
    Create User Serializer.

    Define required fields that for creation and retrieving user
    """

    mails = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Mail.objects.all())

    class Meta:
        """
        Create Meta class for User serializer.

        Define fields and model to serialize here.
        """

        model = User
        fields = ('id', 'username', 'mails', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Create Group serializer.

    Define required fields that for creation and retrieving user groups
    """

    class Meta:
        """
        Create Meta class for Group serializer.

        Define fields and model to serialize here.
        """

        model = Group
        fields = ('url', 'name')


class MailSerializer(serializers.ModelSerializer):
    """
    Create mail serializer.

    Define required fields that are important for creation and retrieving mails
    """

    class Meta:
        """
        Create Meta class for Mail serializer.

        Define fields and model to serialize here.
        """

        model = Mail
        fields = ('id', 'receiver_address', 'mail_subject', 'mail_body',
                  'time_created', 'sent', 'sender', 'sender_address')
        sender = serializers.ReadOnlyField(source='sender.username')
        # sender_address = serializers.ReadOnlyField(source='sender_id.email')
