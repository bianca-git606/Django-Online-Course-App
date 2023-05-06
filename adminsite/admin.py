from django.contrib import admin
from .models import Course, Instructor, Lesson

# customize fields in the admin page

class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']

# add related objects

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
