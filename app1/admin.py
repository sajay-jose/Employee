from django.contrib import admin
from .models import Register
from .models import login
# Register your models here.
admin.site.register(Register)
admin.site.register(login)