from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from . import models

class UserAdmin(BaseUserAdmin):
  ordering = ['id']
  list_display = ['email']
  fieldsets = (
    (None,{'fields':('email','password')}),
    (_('personal Info'),{'fields':()}),
    (
      _('permissions'),
      {
        'fields':(
          'is_active',
          'is_staff',
          'is_superuser',
        )
      }
    ),
    (_('Important dates'),{'fields':('last_login',)}),
  )
  add_fieldsets = (
    (None, {
      'classes':('wide',),
      'fileds':('email','password','password2')
    }),
  )
  

admin.site.register(models.User,UserAdmin)
admin.site.register(models.Genre)
admin.site.register(models.Trivia)


