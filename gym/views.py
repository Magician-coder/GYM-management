from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, DailyAttendance, FeePayment
from .forms import CustomerForm, FeePaymentForm
import datetime

def home(request):
    return render(request, 'home.html')

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def mark_attendance(request):
    if request.method == 'POST':
        membership_number = request.POST.get('membership_number')
        member = get_object_or_404(Member, membership_number=membership_number)
        today = datetime.date.today()
        if DailyAttendance.objects.filter(member=member, date=today).exists():
            message = "Attendance already marked for today."
        else:
            DailyAttendance.objects.create(member=member, date=today, time=datetime.datetime.now().time())
            message = "Attendance marked successfully."
        return render(request, 'mark_attendance.html', {'message': message})
    return render(request, 'mark_attendance.html')

def fee_status(request):
    if request.method == 'POST':
        membership_number = request.POST.get('membership_number')
        try:
            member = Member.objects.get(membership_number=membership_number)
            status = member.get_fee_status()
            fee_status = f"Fee Status: {status}. Monthly Fee: {member.monthly_fee}"
        except Member.DoesNotExist:
            fee_status = "Member not found."
        return render(request, 'fee_status.html', {'fee_status': fee_status})
    return render(request, 'fee_status.html')

def daily_attendance(request):
    today = datetime.date.today()
    attendees = DailyAttendance.objects.filter(date=today)
    return render(request, 'daily_attendance.html', {'attendees': attendees})

def clear_daily_attendance(request):
    if request.method == 'POST':
        membership_number = request.POST.get('membership_number')
        date = request.POST.get('date')
        try:
            member = Member.objects.get(membership_number=membership_number)
            attendance = DailyAttendance.objects.filter(member=member, date=date)
            if attendance.exists():
                attendance.delete()
                message = "Attendance cleared successfully."
            else:
                message = "No attendance found for this member on the given date."
        except Member.DoesNotExist:
            message = "Member not found."
        return render(request, 'clear_daily_attendance.html', {'message': message})
    return render(request, 'clear_daily_attendance.html')

def remove_customer(request):
    if request.method == 'POST':
        membership_number = request.POST.get('membership_number')
        try:
            member = Member.objects.get(membership_number=membership_number)
            member.delete()
            message = "Customer removed successfully."
        except Member.DoesNotExist:
            message = "Customer not found."
        return render(request, 'remove_customer.html', {'message': message})
    return render(request, 'remove_customer.html')

def pay_fees_later(request):
    if request.method == 'POST':
        form = FeePaymentForm(request.POST)
        if form.is_valid():
            membership_number = form.cleaned_data['membership_number']
            amount = form.cleaned_data['amount']
            member = get_object_or_404(Member, membership_number=membership_number)
            FeePayment.objects.create(member=member, amount_paid=amount, date_paid=datetime.date.today())
            member.fee_status = 1  # Update fee status to "Paid"
            member.save()
            return redirect('home')
    else:
        form = FeePaymentForm()
    return render(request, 'pay_fee.html', {'form': form})
