from django.contrib import admin
from jsonfield import JSONField
from django_json_widget.widgets import JSONEditorWidget
from ..models.tool import tool
from oneRing.util.modelParser import modelParser

@admin.register(tool)
class tool_Admin(admin.ModelAdmin):

    fields = modelParser(tool)

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    readonly_fields = ['id',
                       'shortCode']
