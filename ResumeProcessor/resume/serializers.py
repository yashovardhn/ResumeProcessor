from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    """
    This class is responsible for serializing Candidate model instances into JSON format.

    Attributes:
    - model: The Django model class that this serializer is associated with.
    - fields: A list of field names that should be included in the serialized output.

    Methods:
    - None (inherited from serializers.ModelSerializer)

    """

    class Meta:
        """
        Meta class for CandidateSerializer.

        Attributes:
        - model: The Django model class that this serializer is associated with.
        - fields: A list of field names that should be included in the serialized output.

        """

        model = Candidate
        """The Django model class that this serializer is associated with."""

        fields = ['first_name', 'email', 'mobile_number']
        """A list of field names that should be included in the serialized output."""
