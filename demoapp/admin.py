from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


class UserModel(UserAdmin):
    ordering = ('email',)



admin.site.register(CustomUser, UserModel)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Session)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStaff)
admin.site.register(LeaveReportStudent)
admin.site.register(FeedbackStaff)
admin.site.register(FeedbackStudent)
admin.site.register(NotificationStaff)
admin.site.register(NotificationStudent)
admin.site.register(StudentResult)
admin.site.register(StaffUpload)
admin.site.register(StaffDoc)


