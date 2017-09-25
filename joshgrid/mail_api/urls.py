"""URL Definition for JoshGrid application."""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from joshgrid.mail_api import views

urlpatterns = [
    # url(r'^$', views.api_root),
    url(r'^users/$', views.UserList.as_view(), name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),
        name="user-detail"),
    url(r'^mail/$', views.MailList.as_view(), name="mail-list"),
    url(r'^mail/(?P<pk>[0-9]+)/$', views.MailDetail.as_view(),
        name="mail-detail"),
    url(r'^mail/(?P<pk>[0-9]+)/highlight/$',
        views.MailHighlight.as_view(), name="mail-highlight"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
