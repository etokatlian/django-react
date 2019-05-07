"""Summary
"""
from rest_framework import serializers
from leads.models import Lead


class LeadSerializer(serializers.ModelSerializer):

    """Summary
    """

    class Meta:

        """Summary

        Attributes:
            fields (tuple): Description
            model (TYPE): Description
        """

        model = Lead
        fields = ('__all__')
