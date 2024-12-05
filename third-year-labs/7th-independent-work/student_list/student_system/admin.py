from django.contrib import admin
from .models import Student, Grade

class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')
    inlines = [GradeInline]

class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade')
    search_fields = ('student__first_name', 'student__last_name', 'subject')
    list_filter = ('subject', 'grade')
    ordering = ('student', 'subject')
    actions = ['reset_grades']

    def reset_grades(self, request, queryset):
        queryset.update(grade=0)
    reset_grades.short_description = "Reset selected grades to 0"

admin.site.register(Student, StudentAdmin)
admin.site.register(Grade, GradeAdmin)
