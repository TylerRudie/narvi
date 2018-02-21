from django.conf.urls import url, include


urlpatterns = [

    url(r'^api/timeslot/',
        include('oneRing.urls.timeslot')
        ),

    url(r'^api/tool/',
        include('oneRing.urls.tool')
        ),
]