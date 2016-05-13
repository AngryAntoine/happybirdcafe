from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.greeting_page, name='greeting_page'),
]