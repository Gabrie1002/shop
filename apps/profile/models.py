from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
    phone = models.CharField('phone', max_length=20)
    is_active = models.BooleanField('is_active', default=True)

    def __str__(self):
        return self.user.email

    def email(self):
        return self.user.email
