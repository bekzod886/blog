from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . forms import CustomUserCerationForm,CustomUserChangeForm

from . models import CustomUser

# Register your models here.
class CastumUserAdmin(UserAdmin):
    add_form = CustomUserCerationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','age','adress','job']

admin.site.register(CustomUser,CastumUserAdmin)