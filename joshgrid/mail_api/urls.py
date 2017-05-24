from django.conf.urls import url
from joshgrid.mail_api import views

urlpatterns = [
    url(r'^mails/$', views.mail_list),
    url(r'^mails/(?P<pk>[0-9]+)/$', views.mail_detail),
]