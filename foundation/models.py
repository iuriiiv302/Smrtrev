from datetime import datetime

from django.db import models
import factory.django


class Statement(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=32)
    date_create_statement = models.DateTimeField(null=True, blank=True, default=datetime.now())
    INPROCESS = 'inprocess'
    FINISHED = 'finished'
    STATUS_CHOICES = [
        (INPROCESS, 'inprocess'),
        (FINISHED, 'finished'),
    ]
    status_pass = models.CharField(max_length=10, choices=STATUS_CHOICES)


class StatementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Statement

    name = factory.Faker('name')
    surname = factory.Faker('surname')
    phone_number = factory.Faker('phone_number')
    status_pass = factory.Faker("What process is your passport in?")