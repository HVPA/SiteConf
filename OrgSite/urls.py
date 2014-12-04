from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'OrgSite.views.home', name='home'),   
)
