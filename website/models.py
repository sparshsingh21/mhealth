from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Doctor(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#     username = models.CharField(unique=True, max_length=10)
#     speciality = models.CharField(max_length=50)
#     qualification = models.CharField(max_length=20)
#     created_on = models.DateField()
#     created_by = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return "Dr. " + self.first_name + self.last_name