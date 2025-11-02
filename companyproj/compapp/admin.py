from django.contrib import admin
from .models import Employee 

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name','position','joined_on','phone_number')
    search_fields =('name','position')
    list_filter = ('joined_on',)
