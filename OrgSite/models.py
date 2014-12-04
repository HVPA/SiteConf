from django.db import models
from django.contrib.auth.models import User

class OrgSite(models.Model):
    ID = models.AutoField(primary_key=True)
    OrgHashCode = models.CharField("OrgHashCode", max_length=255, blank = True, null = True)
    HVPAdmin = models.NullBooleanField('HVPAdmin', null = True )
    AdminOrgSiteID = models.IntegerField('AdminOrgSiteID', null = True)

    def __unicode__(self):
        return self.OrgHashCode

    class Meta:
        db_table = "OrgSite"
