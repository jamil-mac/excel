from django.db import models


class UserModel(models.Model):
    full_name = models.CharField(max_length=100)
    event_name = models.CharField(max_length=255)
