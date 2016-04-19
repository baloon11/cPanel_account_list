# coding: utf-8
import time
import pycpanel
from django.core.management.base import NoArgsCommand
from application.models import Server, CronTime

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        all_servers=Server.objects.all()
        for curr_server in all_servers:
            server = pycpanel.conn(hostname=curr_server.name,
                                   username=curr_server.login,
                                   password=curr_server.password) #Basic user/password authentication
            curr_server.checking_by_cron='No data'
            try:
                account_list=server.api('listaccts')['acct']
                curr_server.checking_by_cron=str(len(account_list))
                curr_server.save()
            except:
                while curr_server.checking_by_cron=='No data':
                    account_list=server.api('listaccts')['acct']
                    curr_server.checking_by_cron=str(len(account_list))
                    curr_server.save()
                    time.sleep(2)
        try:
            CronTime.objects.get(id=1).save()
        except CronTime.DoesNotExist:
            CronTime.objects.create()




