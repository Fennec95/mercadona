from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models

class ShopperManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse e-mail est obligatoire pour créer un utilisateur.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Shopper(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)


    objects = ShopperManager()

