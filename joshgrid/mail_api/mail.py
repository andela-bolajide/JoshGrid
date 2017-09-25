from celery import shared_task
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

@shared_task
def local_send_email(request):
    print(settings)
    subject = request.POST.get('mail_subject', '')
    message = request.POST.get('mail_body', '')
    from_email = request.POST.get('sender_address', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['cooproton@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/mail/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
