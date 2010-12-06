from django.contrib import admin
from django.contrib.sites.models import Site

from rbwebhooks.models import Webhook


class WebhookAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'class_name')
    fields = ('url',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = Site.objects.get_current()

        obj.save()


print "Hello world!"
admin.site.register(Webhook, WebhookAdmin)
