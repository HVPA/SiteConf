from django.db import models
from OrgSite.models import OrgSite

class Upload (models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField("Name", max_length=255, blank = False, null = True)
    DataSourceType = models.CharField("DataSourceType", max_length=255, blank = True, null = True)
    DataSourceName = models.CharField("DataSourceName", max_length=255, blank = True, null = True)
    DatabaseName = models.CharField("DatabaseName", max_length=255, blank = True, null = True)
    UserName = models.CharField("UserName", max_length=255, blank = True, null = True)
    Password = models.CharField("Password", max_length=255, blank = True, null = True)
    Plugin = models.CharField("Plugin", max_length=255, blank = True, null = True)
    RefMapper = models.CharField("RefMapper", max_length=255, blank = True, null = True)
    OrgSite = models.ForeignKey( OrgSite, blank = True, null = True )
    
    def __unicode__(self):
        return self.Name

    class Meta:
        db_table = "Upload"
