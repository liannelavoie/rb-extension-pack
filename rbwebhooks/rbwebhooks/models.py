from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from djblets.webapi.core import JSONEncoderAdapter
from rbwebhooks.post_url_dispatcher import dispatch as post

class Webhook(models.Model):
    owner_type = models.ForeignKey(ContentType)
    owner_id = models.PositiveIntegerField()
    owner = generic.GenericForeignKey(ct_field="owner_type", fk_field="owner_id")
    
    url = models.URLField()

    def dispatch(self, payload):
        adapter = JSONEncoderAdapter()
        content = adapter.encode(payload)

        post(self.url, {'payload': content})

    def __unicode__(self):
        return self.url
