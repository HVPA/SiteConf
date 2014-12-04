from tastypie.resources import ModelResource
from OrgSite.models import OrgSite

class OrgSiteResource(ModelResource):
    class Meta:
        queryset = OrgSite.objects.all()
        resource_name = 'orgsite'
