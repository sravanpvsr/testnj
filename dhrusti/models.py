from django.db import models
from datetime import datetime


# Create your models here.

class Test(models.Model):
        name = models.CharField(max_length=50)
        date_of_appointment = models.DateField(null=True)
        fname = models.CharField(max_length=50)
        age = models.CharField(max_length=10)
        gender = models.CharField(max_length=10)
        occupation = models.CharField(max_length=50)
        mobile = models.CharField(max_length=50)
        address = models.CharField(max_length=50)
        email = models.EmailField(max_length=50)
        samithi = models.CharField(max_length=50)
        bvguru = models.CharField(max_length=50)
        sai_connect_number = models.CharField(max_length=50)
        city = models.CharField(max_length=50)
        state = models.CharField(max_length=50)
        gradual_decrease_in_vision = models.CharField(max_length=50, null=True)
        sudden_decrease_in_vision = models.CharField(max_length=50, null=True)
        blurred_distant_vision = models.CharField(max_length=50, null=True)
        blurred_near_vision = models.CharField(max_length=50, null=True)
        pain = models.CharField(max_length=50, null=True)
        redness = models.CharField(max_length=50, null=True)
        others = models.TextField(max_length=250, null=True)
        past_history = models.CharField(max_length=50, null=True)
        family_history = models.CharField(max_length=50, null=True)
        Others2 = models.TextField(max_length=250, null=True)
        systemic_disease = models.CharField(max_length=100, null=True)
        others3 = models.TextField(max_length=250, null=True)
        medication = models.CharField(max_length=50, null=True)
        others4 = models.TextField(max_length=250, null=True)
        allergy = models.CharField(max_length=50, null=True)
        created_date = models.DateTimeField(default=datetime.now, blank=True)

        def __str__(self):
            return self.name
