# coding: utf-8
from django import template
from application.models import Server,CronTime


register = template.Library()

@register.inclusion_tag('cron_table.html')
def cron_table():
    try:
        cron_time=CronTime.objects.get(id=1).time
    except CronTime.DoesNotExist:
        cron_time='No data'
    return dict(
        servers = Server.objects.all(),
        cron_time = cron_time
        )