"""Summary
"""
from django.db import models


class Lead(models.Model):

    """Summary

    Attributes:
        created_at (string): Date/Time is created
        email (string): The lead's email address
        message (string): Message associated with the lead
        name (string): The lead's name
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
