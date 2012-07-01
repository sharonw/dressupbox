from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from app.models import User, Dress, Transaction

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('app.views',
    # Static pages
    url(r'^login/$', 'login'),
    url(r'^signup/$', 'signup'),
    url(r'^map/$', 'map'),
    url(r'^dress/$', 'dress'),
    url(r'^moreinfo/$', 'moreinfo'),

    # url(r'^login/$', TemplateView.as_view(template_name='frontend/login.html')),
    # url(r'^signup/$', TemplateView.as_view(template_name='frontend/signup.html')),
    # url(r'^map/$', TemplateView.as_view(template_name='frontend/map.html')),
    # url(r'^dress/$', TemplateView.as_view(template_name='frontend/dress.html')),
    # url(r'^moreinfo/$', TemplateView.as_view(template_name='frontend/moreinfo.html')),

    # Dynamic pages
    url(r'^search/$', 'search'),
    url(r'^results/$', 'results'),

    # Internal pages
    url(r'^admin/', include(admin.site.urls)),
)
