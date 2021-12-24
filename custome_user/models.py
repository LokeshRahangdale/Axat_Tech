from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models.base import Model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustUserManager
# Create your models here.
class CustUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=1000,default="")
    password1 = models.CharField(max_length=1000,default="")
    mobile_num = models.CharField(max_length=1000,default="")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=50, default='', null=True, blank= True)
    disable_reason = models.CharField(max_length=200, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustUserManager()

    def __str__(self):
        return self.email

class student_model(models.Model):
    user   = models.ForeignKey(CustUser, null=True, on_delete=models.CASCADE)
    student_image = models.ImageField(upload_to="Student_image",default="")

class teacher_model(models.Model):
    user   = models.ForeignKey(CustUser, null=True, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="Teacher_image",default="")
    image2 = models.ImageField(upload_to="Teacher_image",default="")
    image3 = models.ImageField(upload_to="Teacher_image",default="")
