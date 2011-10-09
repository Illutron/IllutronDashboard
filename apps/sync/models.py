from django.contrib.auth.models import User
from django.db import models
from apiclient.ext.django_orm import OAuthCredentialsField

class LatitudeCredential(models.Model):
    """
    Model for storing oauth2 token user credentials
    to access private information through latitude api.
    """
    id = models.ForeignKey(User, primary_key=True)
    credential = OAuthCredentialsField()