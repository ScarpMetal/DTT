from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import View
from django.http import HttpResponseRedirect

from dal import autocomplete
# ********** Start Views **********

def main_page(request):
    return render(request, 'autocomplete-widget/index.html', {})

class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Company.objects.none()

        qs = Company.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

# ********** End Views **********
