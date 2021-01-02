from django.db import models

class dataimport(models.Model):
        id = models.AutoField(primary_key=True)
        hour = models.IntegerField(null=True)
        minutes = models.IntegerField(null=True)
        period = models.CharField(max_length=25, null=True)
        province = models.CharField(max_length=50,null=True)
        country = models.CharField(max_length=50,null=True)
        latitude = models.DecimalField(max_digits=9, decimal_places=6,null=True)
        longtitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
        narrative = models.TextField(max_length=50,null=True)

