from django.contrib import admin

from persons.models import Person, Department, Role, Right

admin.site.register(Person)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Right)

# Register your models here.
