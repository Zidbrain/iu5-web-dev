from django.db import models

# Create your models here.


class Company(models.Model):
    idcompany = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class IcecreamToCompany(models.Model):
    icecream_id = models.PositiveIntegerField(primary_key=True)
    company_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'icecream_to_company'
        unique_together = (('icecream_id', 'company_id'),)


class IcecreamTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    image_url = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icecream_types'

