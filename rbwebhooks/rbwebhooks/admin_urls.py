from django.conf.urls.defaults import patterns

from rbwebhooks.extension import WebhooksExtension
from rbwebhooks.forms import WebhooksSettingsForm


urlpatterns = patterns('',
    (r'^$', 'reviewboard.extensions.views.configure_extension',
     {'ext_class': WebhooksExtension,
      'form_class': WebhooksSettingsForm,
    })
)
