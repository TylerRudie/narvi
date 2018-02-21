from django.db import models

from .tool import tool
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import uuid
from oneRing.util.oneTimeCode import genOneTimeCode
from django.utils.timezone import now

from django.utils import timezone


class timeSlot(models.Model):
    id        = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4,
                                 editable=False)

    oneTimeCode = models.CharField(max_length=8,
                                   editable=False,
                                   unique=True,
                                   )

    startTime   = models.DateTimeField()

    endTime     = models.DateTimeField()

    tool        = models.ForeignKey(tool,
                                    on_delete=models.CASCADE)
    user        = models.ForeignKey(User,
                                    on_delete=models.CASCADE)

    @property
    def isValid(self):
        if self.user.usertooldata.isValid is False:
            return False
        elif tool.timeBound == 'n':
            return True
        elif self.startTime > now():
            return False
        elif self.endTime < now():
            return False
        else:
            return True

    def __str__(self):
        return "{} <-> {} < {} |  > ".format(str(timezone.localtime(self.startTime)),
                                               str(timezone.localtime(self.endTime)),
                                               self.tool.name,
                                               )

    def clean(self, *args, **kwargs):

        if not hasattr(self, 'tool') or self.car is None:
            raise ValidationError('No Tool Selected')

        elif self.startTime is None:
            raise ValidationError('Correct Start Time')

        elif self.endTime is None:
            raise ValidationError('Correct End Time')

        else:
            testA = timeSlot.objects.filter(tool=self.tool,
                                            startTime__lte=self.startTime,
                                            endTime__gt=self.startTime).exclude(id=self.id).count()

            testB = timeSlot.objects.filter(tool=self.tool,
                                            startTime__lt=self.endTime,
                                            endTime__gte=self.endTime).exclude(id=self.id).count()

            testC = timeSlot.objects.filter(tool=self.tool,
                                            startTime__gte=self.startTime,
                                            endTime__lte=self.endTime).exclude(id=self.id).count()

            if testA > 0:
                raise ValidationError('Test A Overlap Detected')

            elif testB > 0:
                raise ValidationError('Test B Overlap Detected')

            elif testC > 0:
                raise ValidationError('Test C Overlap Detected')

            else:
                super(timeSlot, self).clean(*args, **kwargs)



    def save(self, *args, **kwargs):
        self.clean()
        if len(self.oneTimeCode) is 0 :
            self.oneTimeCode = genOneTimeCode()
        super(timeSlot, self).save(*args, **kwargs)