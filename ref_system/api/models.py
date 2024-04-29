import random
import string

from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    invite_code = models.CharField(max_length=6, unique=True, null=True, blank=True)
    numbers_activated_invite_codes = ArrayField(models.CharField(max_length=20), blank=True, default=list)
    activated_invite_code = models.CharField(max_length=6, null=True, blank=True, default=None)

    def generate_invite_code(self):
        if not self.invite_code:
            self.invite_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            self.save()

    def add_activated_invite_code(self, phone_number):
        if phone_number not in self.numbers_activated_invite_codes:
            self.numbers_activated_invite_codes.append(phone_number)
            self.save()


class RefCode(models.Model):
    code = models.CharField(max_length=6, null=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.code


class VerificationCode(models.Model):
    verif_code = models.CharField("Verification_code", max_length=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.verif_code
