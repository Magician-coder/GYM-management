import datetime
from django import forms
from django.db import models
from django.core.management.base import BaseCommand

class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    membership_number = models.CharField(max_length=20, unique=True)
    cnic_number = models.CharField(max_length=20, unique=True)
    fee_status = models.IntegerField(default=0)
    joining_date = models.DateField(default=datetime.date.today)
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def get_fee_status(self):
        return "Paid" if self.fee_status > 0 else "Unpaid"

    def __str__(self):
        return self.name

class FeePayment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()

class DailyAttendance(models.Model):
    date = models.DateField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    time = models.TimeField()

class GymMember(models.Model):
    membership_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    cnic_number = models.CharField(max_length=13, unique=True)
    fee_status = models.IntegerField()
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    def __str__(self):
        return self.name
class Command(BaseCommand):
    help = 'Update fee status to unpaid if one month has passed since joining date.'

    def handle(self, *args, **kwargs):
        today = datetime.timezone.now().date()
        one_month_ago = today - datetime.timedelta(days=30)

        members = Member.objects.filter(joining_date__lt=one_month_ago, fee_status__gte=0)
        for member in members:
            member.fee_status = 0  # Set to unpaid
            member.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated fee status for members.'))
class FeePaymentForm(forms.Form):
    membership_number = forms.CharField(max_length=20)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    
    