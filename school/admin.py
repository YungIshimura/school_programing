from django.contrib import admin
from .models import School, Course, School_Courses


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(School_Courses)
class SchoolCoursesAdmin(admin.ModelAdmin):
    pass