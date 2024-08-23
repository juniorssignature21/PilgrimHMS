from django.db import models

# Create your models here.
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"