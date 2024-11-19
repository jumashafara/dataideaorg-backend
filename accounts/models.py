from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name']
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('N', 'N/A')]

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(verbose_name='User email', blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=1, default="N")

    def __str__(self):
        return f'{self.last_name} {self.first_name}'