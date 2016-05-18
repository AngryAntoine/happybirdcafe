# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.feeders_type, name='feeders_types'),
    url(r'^details/(?P<our_feeder_id>[0-9]+)/$', views.feeders_type_details,
        name='feeders_type_details'),
]
