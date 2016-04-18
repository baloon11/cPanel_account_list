# -*- coding: utf-8 -*-
import time
import json
import pycpanel
from django.contrib import auth
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse #,JsonResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import Server,CronTime
from .forms import StartForm


class StartView(FormView):
    form_class = StartForm
    template_name = 'start.html'
    def form_valid(self, form):
        fcd = form.cleaned_data
        user=auth.authenticate(username=fcd['username'], password=fcd['password'])
        if user is not None:
            if user.is_active:
                auth.login(self.request, user)
                return HttpResponseRedirect(reverse('servers'))
            else:
                return render_to_response("start.html",
                                            {'error_start':'This user is disabled (inactive)'},
                                          context_instance=RequestContext(self.request))
        else:
            return render_to_response("start.html",
                                        {'error_start':'Obviously, you have entered wrong username or password.\
                                          Please, try again.'},
                                      context_instance=RequestContext(self.request))


@csrf_exempt
@login_required
def servers (request):
    if request.method == "POST" and request.is_ajax():
        all_servers=Server.objects.all()
        print "start"
        server_list=[]
        for curr_server in all_servers:
            server = pycpanel.conn(hostname=curr_server.name,
                                   username=curr_server.login,
                                   password=curr_server.password) #Basic user/password authentication
            checking_data='No data'
            try:
                account_list=server.api('listaccts')['acct']
                server_list.append([curr_server.name, len(account_list)])
                print "processed server ", curr_server.name
                checking_data=len(account_list)
            except:
                while checking_data=='No data':
                    account_list=server.api('listaccts')['acct']
                    server_list.append([curr_server.name,len(account_list)])
                    checking_data=len(account_list)
                    time.sleep(2)
                print "processed server ", curr_server.name
#        return JsonResponse({"server_list":server_list})
        return HttpResponse(json.dumps({"server_list":server_list}), content_type="application/json")
    else:
        return render_to_response("servers.html",
                                  context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')