from django.shortcuts import render
from service.models import Service
from contact.forms import ContactForm

def home(request):
    services = Service.objects.all()
    contact_form = ContactForm()
    context = dict(
        services=services,
        contact_form=contact_form,
    )
    return render(request, "index.html", context)

