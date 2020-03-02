from django.contrib import admin

from .models import Application, StudentRegistration,StaffRegistration


admin.site.register(Application)
admin.site.register(StudentRegistration)
admin.site.register(StaffRegistration)
