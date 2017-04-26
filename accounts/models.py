from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import UserManager
from abstract.models import AbstractTimeStampModel

# Create your models here.

class AuthUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return "/"


class Teacher(models.Model):
    user = models.OneToOneField(AuthUser, related_name='teacher', primary_key=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    guardian_name = models.CharField(max_length=30, null=True, blank=True)
    contact_no = models.CharField(max_length=13, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Batch(models.Model):
    name = models.CharField(max_length=20, unique=True)
    batch_teacher = models.OneToOneField(Teacher, related_name='batch', null=True, blank=True)
    division = models.CharField(max_length=2, null=True, blank=True)
    strength = models.IntegerField()

    class Meta:
        verbose_name_plural = 'batches'

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(AuthUser, primary_key=True)
    batch = models.ForeignKey(Batch, related_name='students', null=True, blank=True)
    full_name = models.CharField(max_length=30, null=True, blank=True)
    roll_no = models.IntegerField(null=True, blank=True)
    register_no = models.IntegerField(null=True, blank=True)
    guardian_name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    contact_no = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.user.username
