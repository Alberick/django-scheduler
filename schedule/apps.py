from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ScheduleConfig(AppConfig):
    name = 'schedules'
    
    verbose_name = _('Schedules')
