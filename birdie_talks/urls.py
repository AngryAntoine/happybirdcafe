from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.birdie_talks, name='birdie_talks'),
    url(r'^how_to_feed_article/(?P<article_id>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^recommendation_articles/$', views.recommendation_articles, name='recommendation_articles'),
    url(r'^recommendations_details/(?P<recommendation_id>[0-9]+)/$', views.recommendation_detail,
        name='recommendation_detail'),
    url(r'^feeders_type/$', views.feeders_type, name='feeders_types'),
    url(r'^feeders_type_details/(?P<feeder_id>[0-9]+)/$', views.feeders_type_details,
        name='feeders_type_details'),
    url(r'^forum/$', views.forum, name='forum'),
]
