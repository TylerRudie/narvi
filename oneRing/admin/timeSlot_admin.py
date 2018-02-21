from django.contrib import admin
from jsonfield import JSONField

from ..models.timeSlot import timeSlot
from django.db.models import DateTimeField


@admin.register(timeSlot)
class timeSlot_Admin(admin.ModelAdmin):

    readonly_fields = []

    list_display = ['oneTimeCode',
                    'startTime',
                    'endTime',
                    'tool',
                    'user',
                    'isValid'
                    ]

