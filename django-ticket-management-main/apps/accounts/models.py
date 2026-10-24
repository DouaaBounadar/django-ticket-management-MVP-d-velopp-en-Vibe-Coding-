from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
	use_in_migrations = True

	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError('An email address is required.')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('A superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('A superuser must have is_superuser=True.')

		return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
	ROLE_EMPLOYE = 'employe'
	ROLE_TECHNICIEN = 'technicien'
	ROLE_RESPONSABLE = 'responsable'
	ROLE_CHOICES = [
		(ROLE_EMPLOYE, 'Employe'),
		(ROLE_TECHNICIEN, 'Technicien'),
		(ROLE_RESPONSABLE, 'Responsable'),
	]

	username = None
	email = models.EmailField(unique=True)
	role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_EMPLOYE)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()
