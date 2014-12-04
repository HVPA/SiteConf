from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# tastypie restful stuff
from SiteConf.resources import UserResource, DiseaseTagResource, GeneResource, HVPTransactionResource, OrgSiteResource, UploadResource
from tastypie.api import Api
from tastypie.serializers import Serializer

# version 1.0 of tastypie rest api
v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(DiseaseTagResource())
v1_api.register(GeneResource())
v1_api.register(HVPTransactionResource())
v1_api.register(OrgSiteResource())
v1_api.register(UploadResource())
v1_api.serializer = Serializer(formats=['json'])

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SiteConf.views.home', name='home'),
    # url(r'^SiteConf/', include('SiteConf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^upload/', include('Upload.urls')),
    url(r'^orgSite/', include('OrgSite.urls')),
    
    url(r'^api/', include(v1_api.urls)),
)
