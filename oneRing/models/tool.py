from django.db import models
import uuid
from jsonfield import JSONField
from oneRing.util.oneTimeCode import genOneTimeCode
from oneRing.models.toolGroup import toolGroup

mode = (('y','Yes'),
        ('n','No')
       )

class tool(models.Model):
    id           = models.UUIDField(primary_key=True,
                                    default=uuid.uuid4,
                                    editable=False)

    shortCode   = models.CharField(max_length=8,
                                   editable=False,
                                   unique=True,
                                   )

    name         = models.CharField(max_length=30)

    group        = models.ForeignKey(toolGroup,
                                     null=True,
                                     blank=True,
                                     on_delete=models.SET_NULL)

    active       = models.CharField(choices=mode,
                                    max_length=1
                                    )

    defaultBump  = models.IntegerField(default= 0)

    userOTC      = models.CharField(max_length=8,
                                    blank=True,
                                    null=True)

    adminOTC     = models.CharField(max_length=8,
                                    blank=True,
                                    null=True)

    changeOTC_at = models.DateTimeField(blank=True,
                                        null=True)

    timeBound    = models.CharField(choices=mode,
                                    max_length=1
                                    )

    config       = JSONField(null=True,
                             blank=True,)

    @property
    def authUsers(self):
        return [x.usertooldata.cardID for x in self.group.authUsers.all()]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.clean()
        if len(self.oneTimeCode) is 0 :
            self.oneTimeCode = genOneTimeCode()
        super(tool, self).save(*args, **kwargs)