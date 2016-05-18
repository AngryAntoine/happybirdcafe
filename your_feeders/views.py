from django.shortcuts import render, get_object_or_404
from .models import YourFeeder

# Create your views here.


def feeders_type(request):
    your_feeders_types = YourFeeder.objects.all()
    return render(request, 'your_feeders/feeders_type.html',
                  {'your_feeders_types': your_feeders_types})


def feeders_type_details(request, your_feeder_id):
    your_feeders_types = get_object_or_404(YourFeeder, id=your_feeder_id)
    your_feeders_type_detail = get_object_or_404(YourFeeder, id=your_feeder_id)
    return render(request, 'your_feeders/feeders_type_detail.html',
                  {'your_feeders_types': your_feeders_types,
                   'your_feeders_type_detail': your_feeders_type_detail})
