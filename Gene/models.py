from django.db import models
from Upload.models import Upload

class Gene(models.Model):
    ID = models.AutoField(primary_key=True)
    GeneName = models.CharField("GeneName", max_length=255, blank = True, null = True)
    RefSeqName = models.CharField("RefSeqName", max_length=255, blank = True, null = True)
    RefSeqVersion = models.CharField("RefSeqVersion", max_length=255, blank = True, null = True)
    Upload = models.ForeignKey( Upload, blank = True, null = True )

    def __unicode__(self):
        return self.GeneName

    class Meta:
        db_table = "Gene"
