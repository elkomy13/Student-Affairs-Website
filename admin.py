from django.contrib import admin
from .models import ContactUs
from .models import Student
from .models import admins

# Register your models here.
#Data bases
admin.site.register(ContactUs)
admin.site.register(Student)
admin.site.register(admins)

