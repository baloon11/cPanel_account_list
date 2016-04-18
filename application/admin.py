# coding: utf-8
from django.contrib import admin
from django import forms
from .models import Server#, CronTime


class ServerAdminForm(forms.ModelForm):

    class Meta:
        model = Server
        fields = ['name','login','password']


class ServerAdmin(admin.ModelAdmin):
    form =ServerAdminForm
    list_display=('name',)


# class CronTimeAdmin(admin.ModelAdmin):
#     list_display=('time',) 


admin.site.register(Server, ServerAdmin)
# admin.site.register(CronTime, CronTimeAdmin)
