from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    model =User
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    searching_fields = ('email', )
    ordering = ('email', )
    
    fieldsets = (
        ('Autentication', {
            'fields': (
                'email', 'password'
            )
        }),
        ('Permission', {
            'fields': (
                'is_staff', 'is_active', 'is_superuser'
            )
        }),
        ('Group Permission', {
            'fields': (
                'groups', 'user_permissions',
            )
        }),
        ('Important Date', {
            'fields': (
                'last_login',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "is_superuser"
            )}
        ),
    )

# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
