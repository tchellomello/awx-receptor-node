from django.db import models
from django.shortcuts import render

LOG_LEVEL = (
    (u'DEBUG', 'Debug'),
    (u'INFO', 'Info'),
)

LISTENER_PROTOCOL = (
    (u'TCP', 'TCP'),
    (u'UDP', 'UDP'),    
)


class ReceptorControlService(models.Model):
    name = models.CharField(max_length=200, unique=True)
    filename = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'filename')

class ReceptorWorkCommand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    command = models.CharField(max_length=200)
    params =  models.CharField(max_length=200)
    allowruntimeparams = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name',)

class ReceptorCertificate(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class ReceptorNode(models.Model):
    name = models.CharField(max_length=200, unique=True)
    peers = models.ManyToManyField('ReceptorNode', blank=True)
    control_service = models.ForeignKey(
        ReceptorControlService,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    work_commands = models.ManyToManyField('ReceptorWorkCommand', blank=False)

    log_level = models.CharField(max_length=5, choices=LOG_LEVEL)
    listener_protocol = models.CharField(
        max_length=3,
        choices=LISTENER_PROTOCOL,
        default=LISTENER_PROTOCOL[0]
    )
    listener_port = models.IntegerField(default=2222)
    listener_address = models.CharField(max_length=50, blank=False, null=False)
    certificates = models.ForeignKey(
        ReceptorCertificate,
        related_name='certificates',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


    @property
    def render_config(self):
        return render(None, 'receptor_nodes/render_config.html', {'node': self}).content