from django.db import models

# Create your models here.


class Device(models.Model):
    class Meta:
        db_table = 'device'

    ip = models.IntegerField()

    def __str__(self):
        return str(ip)


class Search(models.Model):
    class Meta:
        db_table = 'search'
    item = models.CharField(max_length=45)
    device  = models.ForeignKey('Device', on_delete=models.CASCADE)
