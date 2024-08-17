from django.contrib import admin
from .models import Member, DailyAttendance

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('membership_number', 'name', 'phone_number', 'fee_status')

@admin.register(DailyAttendance)
class DailyAttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'date', 'time')
