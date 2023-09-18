from django.db import models
from django.db import migrations
from django.utils import timezone
from django.utils import timezone
import datetime

from django.contrib.auth.models import User, AbstractUser, Group, Permission

# Create your Data base here.
class ContactUs(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    level = models.IntegerField(default=1)
    department = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=100, default='')
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, default='')
    birth_date = models.DateField(default=datetime.date.today)
    GPA = models.FloatField(default=0.0)

    def _str_(self):
        return self.name



class admins(models.Model):  # admin login with email and password
    userName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    verifyPassword = models.CharField(max_length=100)

    def _str_(self):
        return self.userName


