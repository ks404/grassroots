from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Voter

class ProfileView(generic.DetailView):
    model = Voter
    template_name = 'core/profile.html'
