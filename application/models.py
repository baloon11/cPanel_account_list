# coding: utf-8
from django.db import models


class Server(models.Model):
    name=models.CharField(verbose_name='Server',max_length=300)
    login=models.CharField(verbose_name='Login',max_length=300)
    password=models.CharField(verbose_name='Password',max_length=300)
    checking_by_cron=models.CharField(verbose_name='Checking by cron',default="No data", max_length=50, blank=True)

    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Servers"

    def __unicode__(self):
        return ' server %s ' % self.name


class CronTime(models.Model):
    time=models.DateTimeField(verbose_name='time of last update data by crone', auto_now=True)

    def __unicode__(self):
        return ' server %s ' % self.time
