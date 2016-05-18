from django.shortcuts import render, get_object_or_404
from .models import OurFeeder

# Create your views here.


def feeders_type(request):
    our_feeders_types = OurFeeder.objects.all()
    return render(request, 'our_feeders/feeders_type.html',
                  {'our_feeders_types': our_feeders_types})


def feeders_type_details(request, our_feeder_id):
    our_feeders_types = get_object_or_404(OurFeeder, id=our_feeder_id)
    our_feeders_type_detail = get_object_or_404(OurFeeder, id=our_feeder_id)
    return render(request, 'our_feeders/feeders_type_detail.html',
                  {'our_feeders_types': our_feeders_types,
                   'our_feeders_type_detail': our_feeders_type_detail})
