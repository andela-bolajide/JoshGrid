from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from joshgrid.mail_api import views

urlpatterns = [
    url(r'^mails/$', views.MailList.as_view(), name="create"),
    url(r'^mails/(?P<pk>[0-9]+)/$', views.MailDetail.as_view(), name="retrieve"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
