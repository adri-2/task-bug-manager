from django.contrib import admin
from .models import BugAssignment,BugReport,Category


# Register your models here.
admin.site.register(BugAssignment)
admin.site.register(BugReport)
admin.site.register(Category)
