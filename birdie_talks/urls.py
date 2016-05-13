from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.birdie_talks, name='birdie_talks'),
]
