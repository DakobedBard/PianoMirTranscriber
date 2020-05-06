from django.db import models
from django.conf import settings

class EC2Instance(models.Model):
    '''
    There is a default field with name "id" which is auto increment..
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    instance_ID = models.CharField(max_length=30)
    instance_dns = models.CharField(max_length=80, default="")
    application = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
