from django.contrib import admin
from .models import Test

# Register your models here.
class TestAdmin(admin.ModelAdmin):
    list_display=('id','name','date_of_appointment','occupation','mobile','city')

admin.site.register(Test,TestAdmin)
