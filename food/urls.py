# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.food, name='food'),
    url(r'^details/(?P<food_id>[0-9]+)/$', views.food_details,
        name='food_details'),
]
