from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, date
from django.urls import reverse


# Create your models here.

class User(AbstractUser):
    pin = models.IntegerField(null=True)
    is_customer = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)


GENDER = [('M', 'Male'), ('F', 'Female')]
CARD = [('APL', 'APL'), ('BPL', 'BPL')]
CAST = [('General', 'GENERAL'), ('OBC', 'OBC'), ('SC/ST', 'SC/ST')]
GAS = [('Y', 'YES'), ('N', 'NO')]


class KickCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    # RatonId = models.IntegerField(null=False,unique=True,primary_key=True)
    KickCardNumber = models.IntegerField(null=False, blank=False, unique=True)
    CardType = models.CharField(max_length=10, choices=CARD, null=False, default='APL')
    IssuedDate = models.DateField(verbose_name="Issued Card Date")
    ShopkeeperName = models.CharField(max_length=30, null=False)
    ShopRegisterNumber = models.CharField(max_length=12, verbose_name="Registered Shop Number", null=False)
    CustomerFullName = models.CharField(max_length=35, verbose_name="Customer's Full Name", null=False)
    FirstName = models.CharField(max_length=30, verbose_name="Customer's First Name", null=False)
    LastName = models.CharField(max_length=20, verbose_name="Customer's Last Name", null=False)
    FatherOrHusbandName = models.CharField(max_length=20, verbose_name="Customer's Father/Husband Name", null=False)
    BirthDate = models.DateField(blank=False)
    MotherName = models.CharField(max_length=20, verbose_name="Mother's name", null=False)
    Caste = models.CharField(max_length=30, choices=CAST, null=False, default='general')
    Profession = models.CharField(max_length=20, null=False)
    TotalIncome = models.IntegerField(null=False)
    Address = models.TextField(max_length=100, null=False)
    GasConnection = models.CharField(max_length=10, choices=GAS, verbose_name="Gas Connection", null=False, default='Y')
    VoterIdNumber = models.CharField(max_length=10, unique=True, blank=True)
    AadharCardNumber = models.CharField(max_length=12, unique=True, blank=False)
    PastCard = models.CharField(max_length=12, verbose_name="Past Kick Card Number if Exist", null=True, blank=True)
    TotalMembers = models.PositiveIntegerField(null=False)

    # def get_absolute_url(self):
    #     return reverse('index')

    def __str__(self):
        return self.CustomerFullName


class CancelKickCard(models.Model):
    cancel = models.OneToOneField(KickCard, on_delete=models.CASCADE, related_name='cancel')

    def __str__(self):
        return self.cancel.CustomerFullName


class BookedRation(models.Model):
    booked = models.OneToOneField(KickCard, on_delete=models.CASCADE, related_name='booked', default=True)

    def __str__(self):
        return self.booked.CustomerFullName


class ContectUs(models.Model):
    name = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name
