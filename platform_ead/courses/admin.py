from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date' , 'created_at','image']
    search_fields = ['name']
    # prepopulated_fields = {"slug":("name",)}

admin.site.register(Course, CourseAdmin)