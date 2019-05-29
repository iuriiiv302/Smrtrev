from datetime import datetime

from django.db import models


class Statement(models.Model):
    name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    number = models.IntegerField()
    date_create_statement = models.DateTimeField(null=True, blank=True, default=datetime.now())
    INPROCESS = 'inprocess'
    FINISHED = 'finished'
    STATUS_CHOICES = [
        (INPROCESS, 'inprocess'),
        (FINISHED, 'finished'),
    ]
    status_pass = models.CharField(max_length=10, choices=STATUS_CHOICES)
