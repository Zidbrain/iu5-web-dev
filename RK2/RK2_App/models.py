from django.db import models

# Create your models here.


class Book(models.Model):
    idbook = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=30, blank=True, null=True)
    pages_count = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=15, blank=True, null=True)
    idlabrary = models.ForeignKey('Library', models.DO_NOTHING, db_column='idlabrary', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class Library(models.Model):
    idlibrary = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library'
