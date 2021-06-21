from django.contrib import admin
from .models import Student, State, Score, ExtendedUser
from import_export.admin import ImportExportModelAdmin
from .models import State

# Register your models here.
admin.site.register(Student)
#admin.site.register(State)
admin.site.register(Score)
admin.site.register(ExtendedUser)

@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    pass
