""" Serializers to verify the tables' fields """

from rest_framework import serializers
from showcatalog.models import Show


class ShowSerializer(serializers.ModelSerializer):
    """Verify Show Fields"""

    class Meta:
        model = Show
        fields = ['id', 'name', 'start_year', 'end_year', 'rating', 'age_rating']

