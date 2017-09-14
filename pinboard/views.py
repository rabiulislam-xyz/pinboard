from django.shortcuts import render
from django.views import generic

from .models import Pin, Tag


class IndexListView(generic.ListView):
    model = Pin
    template_name = 'pinboard/index.html'
    paginate_by = 12


class PinDetailView(generic.DetailView):
    model = Pin
    template_name = 'pinboard/pin_detail.html'

def createsuperuserview(request):
    try:
        import os
        from django.contrib.auth.models import User

        username  = os.getenv('USERNAME')
        email     = os.getenv('EMAIL')
        password  = os.getenv('PASSWORD')

        User.objects.create_superuser(username,email,password)

        return HttpResponse("User {} created".format())
    except Exception as e:
        return HttpResponse("{}".format(e))
