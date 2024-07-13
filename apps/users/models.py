import os

from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.image_path import upload_avatar_for_user


class CustomUser(AbstractUser):
<<<<<<< HEAD

=======
>>>>>>> 9c6317ef3439a1adddcd3caa9d23c13314531de4
    avatar = models.ImageField(
        upload_to=upload_avatar_for_user,
        verbose_name='Аватар',
        null=True,
        blank=True,
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.avatar.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.username
