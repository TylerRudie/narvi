from django.conf.urls import url, include
from oneRing.restInterface.timeSlot.validate_v1 import timeSlot_validate_interface


urlpatterns = [

    url(r'^v1/validate/(?P<oneTimeCode>[0-9a-zA-Z_-]+)$',
        timeSlot_validate_interface.as_view(),
        name= 'timeSlot_validate'
        )
    ]