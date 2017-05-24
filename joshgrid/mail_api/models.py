from django.db import models

# Create your models here.
class Mail(models.Model):
    """
    Define the schema for the mail to be sent by a user.

    Here, we define the different parameters required when a user wants to
    send a mail.
    """
    sender_address = models.CharField(max_length=100)
    sender_name = models.CharField(max_length=100, blank=True, default='')
    receiver_name = models.CharField(max_length=100, blank=True, default='')
    receiver_address = models.CharField(max_length=100)
    mail_subject = models.CharField(max_length=100)
    mail_body = models.TextField()
    sent = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('time_created',)

    def __str__(self):
        return "{}".format(self.mail_subject)
