from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.serializers import Serializer
from tastypie import fields
from tastypie.models import create_api_key
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization

from django.contrib.auth.models import User
from django.db import models
from DiseaseTag.models import DiseaseTag
from Gene.models import Gene
from HVPTran.models import HVPTransaction
from OrgSite.models import OrgSite
from Upload.models import Upload


# generates an api_key whe new user is created
models.signals.post_save.connect(create_api_key, sender=User)

# serialise to json format
json_serializer = Serializer(formats=['json'])

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'        
        serializer = json_serializer
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        allowed_method = ['get']
        filtering = {
            'ID': ['exact'],
        }
        max_limit = None


class OrgSiteResource(ModelResource):
    class Meta:
        queryset = OrgSite.objects.all()
        resource_name = 'orgsite'        
        serializer = json_serializer
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        allowed_method = ['get']
        filtering = {
            'ID': ['exact'],
            'OrgHashCode': ['exact'],
            'HVPAdmin': ['exact'],
            'AdminOrgSiteID': ['exact'],
        }
        max_limit = None


class HVPTransactionResource(ModelResource):
    orgsite = fields.ForeignKey(OrgSiteResource, 'OrgSite')

    class Meta:
        queryset = HVPTransaction.objects.all()
        resource_name = 'hvptran'
        serializer = json_serializer
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        allowed_method = ['get', 'post']
        filtering = {
            'orgsite': ALL_WITH_RELATIONS,
        }
        max_limit = None


class UploadResource(ModelResource):
    orgsite = fields.ForeignKey(OrgSiteResource, 'OrgSite')

    class Meta:
        queryset = Upload.objects.all()
        resource_name = 'upload'
        serializer = json_serializer
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        allowed_method = ['get', 'post', 'put']
        filtering = {
            'orgsite': ALL_WITH_RELATIONS,
            'ID': ['exact'],
            'DataSourceType': ['exact']
        }
        max_limit = None


class GeneResource(ModelResource):
    upload = fields.ForeignKey(UploadResource, 'Upload')

    class Meta:
        queryset = Gene.objects.all()
        resource_name = 'gene'
        serializer = json_serializer
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        allowed_method = ['get', 'post', 'put', 'delete']
        filtering = {
            'ID': ['exact'],            
            'upload': ALL_WITH_RELATIONS,
            'GeneName': ['exact', 'icontains'],
            'RefSeqName': ['exact', 'iexact'],
            'RefSeqVersion': ['exact'],
        }
        max_limit = None


class DiseaseTagResource(ModelResource):
    gene = fields.ForeignKey(GeneResource, 'Gene')
    
    class Meta:
        queryset = DiseaseTag.objects.all()
        resource_name = 'diseasetag'
        serializer = json_serializer
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        allowed_method = ['get', 'post', 'put', 'delete']
        filtering = {
            'ID': ['exact'],
            'gene': ALL_WITH_RELATIONS,
        }
        max_limit = None


