from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import UserManager
from abstract.models import AbstractTimeStampModel

# Create your models here.

class AuthUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email

    # def get_absolute_url(self):
    #     return "profiles/"


class Teacher(models.Model):
    user = models.OneToOneField(AuthUser, primary_key=True)
    name = models.CharField(max_length=32, null=True)
    contact_no = models.CharField(max_length=13, blank=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Batch(models.Model):
	name = models.CharField(max_length=10, unique=True)
	division = models.CharField(max_length=2, null=True, blank=True)
	strength = models.IntegerField()

	def __str__(self):
		return self.name


class Student(models.Model):
    user = models.OneToOneField(AuthUser, primary_key=True)
    batch = models.ForeignKey(Batch, related_name='students', null=True, blank=True)
    name = models.CharField(max_length=30)
    roll_no = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name