from django.db import models

class Candidate(models.Model):
    """
    This class represents a Candidate model in a Django application.

    Attributes:
    - first_name: A CharField that stores the candidate's first name.
    - email: An EmailField that stores the candidate's email address.
    - mobile_number: A CharField that stores the candidate's mobile number.

    Methods:
    - __str__: A method that returns the candidate's first name when the object is converted to a string.

    """

    first_name = models.CharField(max_length=100)
    """A CharField that stores the candidate's first name."""

    email = models.EmailField()
    """An EmailField that stores the candidate's email address."""

    mobile_number = models.CharField(max_length=20)
    """A CharField that stores the candidate's mobile number."""

    def __str__(self):
        """Returns the candidate's first name when the object is converted to a string."""
        return self.first_name
