from django.contrib import admin
from .models import Employee
from .models import Company
from .models import Contact


admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Contact)
