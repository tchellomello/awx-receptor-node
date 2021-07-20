from django.contrib import admin
from .models import (
    ReceptorNode, ReceptorCertificate, ReceptorControlService,
    ReceptorWorkCommand
)

admin.site.register(ReceptorNode)
admin.site.register(ReceptorCertificate)
admin.site.register(ReceptorControlService)
admin.site.register(ReceptorWorkCommand)

