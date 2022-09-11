from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=80)

    user_password = models.CharField(max_length=50)

    likes = models.IntegerField()
