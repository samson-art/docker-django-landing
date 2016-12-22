from django.db import models


class Decor(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
