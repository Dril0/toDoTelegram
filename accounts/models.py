from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    """heredamos todas las funcionalidades de AbstractUser para poder modificar o añadir nuevas funcionalidades"""

    pass
