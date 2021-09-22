from django.db import models

# Create your models here.


class crudEmployee(models.Model):
    emp_name = models.CharField(max_length=100, default='')
    emp_age = models.IntegerField()
    emp_phone = models.CharField(max_length=15, default='')
    gender = models.CharField(default='', max_length=1)
    salary = models.FloatField(default=0)
