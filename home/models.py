import datetime
import json
from time import time
from django.db.models.functions import TruncMonth, Length
from django.db.models import Count
import random
import string



import jwt
import requests
from creditcards.models import (CardExpiryField, CardNumberField,
                                SecurityCodeField)
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='photo/user', blank=True)
    city = models.CharField(max_length=50, default="not-provided")
    country = models.CharField(max_length=50, default="not-provided")
    gender = models.CharField(max_length=6, choices=(('Male','Male'), ('Female','Female')), blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    # email = models.EmailField(unique=True)


class Ride(models.Model):
    name = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='photo/ride', blank=True)
    no_of_bags = models.IntegerField()
    no_of_passengers = models.IntegerField()

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=250)


    def __str__(self):
        return self.question


class Policy(models.Model):
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.content



class CustomerMessage(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    phone_number = PhoneNumberField(blank=True, null=True)
    closed = models.BooleanField(default=False)


    def __str__(self):
        return self.full_name


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    price = models.IntegerField()


    def __str__(self):
        return f'{self.source} -- {self.destination}'