from django.shortcuts import render
from .models import Contacts

# Create your views here.


def contacts(request):
    contact = Contacts.objects.all()
    return render(request, 'contacts/contacts.html',
                  {'contact': contact})
