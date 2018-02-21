from django.conf.urls import url, include
from oneRing.restInterface.tool.toolDetail_v1 import toolDetail_interface


urlpatterns = [

    url(r'^v1/detail/(?P<shortCode>[0-9a-zA-Z_-]+)$',
        toolDetail_interface.as_view(),
        name= 'tool_detail'
        )
    ]