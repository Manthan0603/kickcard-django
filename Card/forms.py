from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import DateField
from django.forms.widgets import DateInput
from .models import *


class CustomerSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    pin = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()
    is_donor = forms.BooleanField(label="Register as a Donor", required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'pin', 'is_donor', ]

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_customer = True
            if commit:
                user.save()
            return user


class AddRationCard(forms.ModelForm):
    class Meta:
        model = KickCard
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'RationCardNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'CardType': forms.Select(attrs={'class': 'form-control'}),
            'IssuedDate': forms.DateInput(format='%d/%m/%Y',
                                          attrs={'placeholder': '__/__/____', 'class': 'form-control'}),
            'ShopkeeperName': forms.TextInput(attrs={'class': 'form-control'}),
            'ShopRegisterNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'CustomerFullName': forms.TextInput(attrs={'class': 'form-control'}),
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'FatherOrHusbandName': forms.TextInput(attrs={'class': 'form-control'}),
            'BirthDate': forms.DateInput(attrs={'placeholder': '__/__/____', 'class': 'date form-control'}),
            'MotherName': forms.TextInput(attrs={'class': 'form-control'}),
            'Caste': forms.Select(attrs={'class': 'form-control'}),
            'Profession': forms.TextInput(attrs={'class': 'form-control'}),
            'TotalIncome': forms.NumberInput(attrs={'class': 'form-control'}),
            'Address': forms.Textarea(attrs={'class': 'form-control'}),
            'GasConnection': forms.Select(attrs={'class': 'form-control'}),
            'VoterIdNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'AadharCardNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'PastCard': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'TotalUnit': forms.NumberInput(attrs={'class': 'form-control'}),
            'TotalMembers': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # def save(self, commit: True):
    #     rationdata = super().save(commit=False)
    #     return super().save(commit=)


class Cancelform(forms.ModelForm):
    class Meta:
        model = CancelKickCard
        fields = ['cancel']
        widgets = {'cancel': forms.HiddenInput()}


class Booked(forms.ModelForm):
    booked = forms.BooleanField(disabled=True)

    class Meta:
        model = BookedRation
        fields = ['booked']
        widgets = {'booked': forms.HiddenInput()}


