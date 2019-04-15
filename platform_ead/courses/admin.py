from django.contrib import admin

from platform_ead.courses.models import (Course, Enrollment, Announcement, Comment,Lesson, Material)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date' , 'created_at', 'author', 'image']
    search_fields = ['name']
    prepopulated_fields = {"slug":("name",)}

class MaterialInlineAdmin(admin.TabularInline):

    model = Material

class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name','description']
    list_filter = ['created_at']

    inlines = [
        MaterialInlineAdmin
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement,Comment])
admin.site.register(Lesson, LessonAdmin)
