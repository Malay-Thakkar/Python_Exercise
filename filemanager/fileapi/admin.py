from django.contrib import admin
from .models import signup,filesModel

# class FilesModelAdmin(admin.ModelAdmin):
#     change_form_template = 'progressbarupload/change_form.html'
#     add_form_template = 'progressbarupload/change_form.html'

# admin.site.register(filesModel, FilesModelAdmin)


# Register your models here.
admin.site.register(signup)
admin.site.register(filesModel)
