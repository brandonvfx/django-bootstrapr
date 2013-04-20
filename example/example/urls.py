from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^base/', TemplateView.as_view(template_name="base_test.html")),
    url(r'^base_fluid/', TemplateView.as_view(template_name="base_fluid_test.html")),
    url(r'^base_hero/', TemplateView.as_view(template_name="base_hero_test.html")),
    url(r'^base_masthead/', TemplateView.as_view(template_name="base_masthead_test.html")),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
