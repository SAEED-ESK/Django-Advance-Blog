from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    model =User
    list_display = ('email', 'is_superuser', 'is_active', 'is_verified')
    list_filter = ('email', 'is_superuser', 'is_active', 'is_verified')
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
                'is_staff', 'is_active', 'is_superuser', 'is_verified'
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
                "is_active", "is_superuser", 'is_verified'
            )}
        ),
    )

# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
