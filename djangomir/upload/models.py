from django.db import models
from rest_framework.reverse import reverse
from django.conf import settings


class DocumentFile(models.Model):
    file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=30, default="document.txt")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default =1 )
    def __str__(self):
        return "The dioc is " + self.name + " and the user is " + self.user
