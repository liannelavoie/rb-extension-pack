from django import forms
from django.utils.translation import ugettext as _
from djblets.extensions.forms import SettingsForm


class WebhooksSettingsForm(SettingsForm):
    url = forms.URLField(initial="",
                            help_text=_("The script to run when a signal is received."))
