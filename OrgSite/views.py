from django.shortcuts import render, HttpResponse
from OrgSite.models import OrgSite
from django.core import serializers

def home(request):
    #value = OrgSite.objects.all()    
    value = OrgSite.objects.filter(OrgHashCode__icontains = "test")
    json =  serializers.serialize("json", value, fields=('pk', 'OrgHashCode'))
    
    return HttpResponse(json, mimetype="application/json")


def SiteID(request, orgHashCode):
    value = OrgSite.objects.filter(OrgHashCode = orgHashCode)
    json = serializers.serialize("json", value)

    return HttpResponse(json, mimetype="application/json")
