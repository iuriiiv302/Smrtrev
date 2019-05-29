from .models import Statement
from rest_framework import serializers


class StatementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statement
        fields = ('name', 'surname', 'phone_number', 'date_create_statement', 'status_pass')
