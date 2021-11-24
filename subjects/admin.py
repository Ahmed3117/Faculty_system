from django.contrib import admin
from .models import Subject,Lecture,Department, Branch, Grade, Assignment,Doctor
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_name',)
    prepopulated_fields = {'slug': ('doctor_name',)}

admin.site.register(Subject)
admin.site.register(Lecture)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Department)
admin.site.register(Branch)
admin.site.register(Grade)
admin.site.register(Assignment)
