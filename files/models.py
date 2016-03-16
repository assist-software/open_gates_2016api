from django.db import models
from django.contrib.auth.models import User


class AppFile(models.Model):
    file = models.FileField(upload_to='app_files/')
    user = models.ForeignKey(User)
    comment = models.TextField(null=True, blank=True)
