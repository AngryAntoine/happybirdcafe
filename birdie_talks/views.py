from django.shortcuts import render, get_object_or_404
from .models import Article, Recommendation, Feeder


def birdie_talks(request):
    articles = Article.objects.all()
    return render(request, 'birdie_talks/lets_talk_about_the_birds.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'birdie_talks/how_to_feed_article_detail.html', {'article': article})


def recommendation_articles(request):
    recommendations = Recommendation.objects.all()
    return render(request, 'birdie_talks/recommendation_articles.html', {'recommendations': recommendations})


def recommendation_detail(request, recommendation_id):
    recommendation = get_object_or_404(Recommendation, pk=recommendation_id)
    return render(request, 'birdie_talks/recommendation_detail.html', {'recommendation': recommendation})


def feeders_type(request):
    feeders_types = Feeder.objects.all()
    return render(request, 'birdie_talks/feeders_type.html', {'feeders_types': feeders_types})


def feeders_type_details(request, feeder_id):
    feeders_type_detail = get_object_or_404(Feeder, pk=feeder_id)
    return render(request, 'birdie_talks/feeders_type_detail.html', {'feeders_type_detail': feeders_type_detail})


def forum(request):
    return render(request, 'birdie_talks/forum.html')
