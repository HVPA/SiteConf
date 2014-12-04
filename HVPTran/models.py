from django.db import models
from OrgSite.models import OrgSite

class HVPTransaction(models.Model):
    ID = models.AutoField(primary_key=True)
    Date = models.DateField('Date', blank = False, null = True)
    Who = models.CharField("Who", max_length=255, blank = True, null = True)
    Log = models.CharField("Log", max_length=255, blank = True, null = True)
    Location = models.CharField("Location", max_length=255, blank = True, null = True)
    Byte = models.CharField("Byte", max_length=255, blank = True, null = True)
    OrgSite = models.ForeignKey( OrgSite, blank = True, null = True )

    def __unicode__(self):
        return self.Date

    class Meta:
        db_table = "HVPTransaction"
