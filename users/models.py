from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    )
    STUDENT = 1
    WORKER = 2
    PRESIDENT = 3
    MILITARY = 4
    POS_CHOICE = (
        ("STUDENT", "STUDENT"),
        ("WORKER", "WORKER"),
        ("PRESIDENT", "PRESIDENT"),
        ("MILITARY", "MILITARY")
    )
    phone_number = models.CharField("phone_number", max_length=50)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name="Пол", null=True)
    age = models.IntegerField(null=True, unique=True)
    position = models.CharField(choices=POS_CHOICE, max_length=60, null=True)




