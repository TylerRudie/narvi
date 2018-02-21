from django.contrib import admin
from .tool_admin import tool_Admin
from .timeSlot_admin import timeSlot_Admin
from ..models.timeSlot import timeSlot
from ..models.userToolData import userToolData
from ..models.toolGroup import toolGroup



admin.site.register(toolGroup)

admin.site.register(userToolData)