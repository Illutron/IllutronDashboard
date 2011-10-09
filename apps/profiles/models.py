from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True)
    image = ImageField(
        upload_to='images/profiles/',
        blank=True,
        null=True,
    )
    