
from rest_framework import generics, serializers
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from oneRing.models.timeSlot import timeSlot

class timeSlot_serializer(serializers.ModelSerializer):

    class Meta:
        model  = timeSlot
        fields = ('oneTimeCode',
                  'isValid',
                  'endTime',
        )


class timeSlot_validate_interface(generics.RetrieveAPIView):
    authentication_classes = {TokenAuthentication,
                              SessionAuthentication}

    queryset = timeSlot.objects.all()
    serializer_class = timeSlot_serializer
    lookup_field = ('oneTimeCode')