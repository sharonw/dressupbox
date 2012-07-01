from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from app.models import User, Dress, Transaction

# To implement more views, see Part 3 of the official Django tutorial:
# https://docs.djangoproject.com/en/dev/intro/tutorial03/

# Navigation bar for public pages

nav_list = {'login':    'frontend/login.html',
            'signup':   'frontend/signup.html',
            'map':      'frontend/map.html',
            'dress':    'frontend/dress.html',
            'moreinfo': 'frontend/moreinfo.html'}

# User pages (requires login)

def search(request):
    return render_to_response('frontend/need.html')

def results(request):
    # Even though we claim this is a search response, this is actually all dresses.
    # We know that. We just haven't implemented search yet.
    all_dresses = Dress.objects.all()
    return render_to_response('frontend/results.html', {'all_dresses': all_dresses})

# Public pages (does not require login)

def login(request):
    return render_to_response('frontend/login.html', {'nav_list': nav_list})

def signup(request):
    return render_to_response('frontend/signup.html', {'nav_list': nav_list})

def map(request):
    return render_to_response('frontend/map.html', {'nav_list': nav_list})

def dress(request):
    return render_to_response('frontend/dress.html', {'nav_list': nav_list})

def moreinfo(request):
    return render_to_response('frontend/moreinfo.html', {'nav_list': nav_list})