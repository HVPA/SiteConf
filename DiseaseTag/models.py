from django.db import models
from Gene.models import Gene

class DiseaseTag(models.Model):
    ID = models.AutoField(primary_key=True)
    Tag = models.CharField("Tag", max_length=255, blank = True, null = True)
    Gene = models.ForeignKey( Gene, blank = True, null = True )

    def __unicode__(self):
        return self.Tag

    class Meta:
        db_table = "DiseaseTag"
