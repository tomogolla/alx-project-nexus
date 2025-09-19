from django.contrib import admin
from .models import Category, JobPosting, Location


admin.site.register(Category)
admin.site.register(JobPosting)
admin.site.register(Location)