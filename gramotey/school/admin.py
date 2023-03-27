from django.contrib import admin
from school.models import Teacher, Category, Student, Graduate, Licence

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image',)

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'image',)

# class GraduatesAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'image',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, TeacherAdmin)
admin.site.register(Graduate, TeacherAdmin)

admin.site.register(Category)
admin.site.register(Licence)

