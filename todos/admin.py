# todos/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Campos para listagem
    list_display = ('email', 'name', 'is_active', 'is_staff')
    
    # Campos para edição
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('name', 'phone', 'birth_date')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Campos para criação de usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    
    # Ordenação
    ordering = ('email',)
    
    # Filtros
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    
    # Campos de busca
    search_fields = ('email', 'name')

admin.site.register(User, CustomUserAdmin)