from django.utils import timezone
from rest_framework import generics, serializers
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response

from oneRing.util.modelParser import modelParser
from oneRing.models.tool import tool
from oneRing.models.timeSlot import timeSlot
from oneRing.models.userToolData import userToolData

class group_Serlizer(serializers.ModelSerializer):

    class Meta:
        model = userToolData
        fields = ['authUser',
                  ]



class timeSlot_Serializer(serializers.ModelSerializer):

    class Meta:
        model = timeSlot
        fields = ['oneTimeCode',
                  'startTime',
                  'endTime'
                  ]


class tool_Serializer(serializers.ModelSerializer):
    ## TODO Fliter for timeslots that are only x hours old
    timeslot_set = timeSlot_Serializer(read_only=True,  many=True)


    class Meta:
        model = tool
        fields = ["shortCode",
                  "active",
                  "userOTC",
                  "adminOTC",
                  "config",
                  'timeslot_set',
                  'authUsers']


class toolDetail_interface(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,
                              SessionAuthentication,)

    queryset = tool.objects.all()
    serializer_class = tool_Serializer
    lookup_field = ('shortCode')
