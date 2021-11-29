from django.db import models

# Create your models here.


class Student(models.Model):
    idstudent = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    middle_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'
