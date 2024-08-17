from django import forms
from .models import Member
from .models import GymMember

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'age', 'phone_number', 'membership_number', 'cnic_number', 'monthly_fee']
        widgets = {
            'joining_date': forms.SelectDateWidget(years=range(1900, 2100)),
        }

class FeePaymentForm(forms.Form):
    membership_number = forms.CharField(max_length=20)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
        
