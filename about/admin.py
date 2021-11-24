from django.contrib import admin
from .models import Faculty
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ('faculty_name','description',)
    prepopulated_fields = {'slug': ('faculty_name',)}

admin.site.register(Faculty, AboutAdmin)
