from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

ANIMAL_CHOICES = (
    ('Cat', 'CAT'),
    ('Dog', 'DOG'),
)

AGE_CHOICES = (
    ('Young', 'YOUNG'),
    ('Old', 'OLD'),
)

GENDER_CHOICES = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
)


class Animal(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='media/')
    description = models.TextField(max_length=360)
    difficulty = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    animal = models.CharField(choices=ANIMAL_CHOICES, max_length=3)
    age = models.CharField(choices=AGE_CHOICES, max_length=5)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    sheltered = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
