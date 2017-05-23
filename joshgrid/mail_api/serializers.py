from rest_framework import serializers

from joshgrid.mail_api.models import Mail


class MailSerializer(serializers.Serializer):
    """
    Define Serializer for sending Mails.
    """
    id = serializers.IntegerField(read_only=True)
    sender_address = serializers.EmailField(required=True, max_length=100)
    sender_name = serializers.CharField(max_length=100, allow_blank=True)
    receiver_name = serializers.CharField(max_length=100, allow_blank=True)
    receiver_address = serializers.EmailField(max_length=100)
    mail_subject = serializers.CharField(max_length=100)
    mail_body = serializers.CharField()
    sent = serializers.BooleanField()
    delivered = serializers.BooleanField()
    read = serializers.BooleanField()
    time_created = serializers.DateTimeField()
    time_sent = serializers.DateTimeField(allow_blank=True)
    time_delivered = serializers.DateTimeField(allow_blank=True)
    time_read = serializers.DateTimeField(allow_blank=True)


    def create(self, validated_data):
        """
        Create and return a new `Mail` instance, given the validated data.
        """
        return Mail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Mail` instance, given the validated data.
        """
        instance.mail_subject = validated_data.get('mail_subject', instance.mail_subject)
        instance.mail_body = validated_data.get('mail_body', instance.mail_body)
        instance.receiver_address = validated_data.get(
            'receiver_address', instance.receiver_address)
        instance.save()
        return instance
