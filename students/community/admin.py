from django.contrib import admin
from .models import UserLogin,postUser,Discussion

class UserLoginAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'datetime', 'is_active', 'mobile', 'profession', 'field')

# Register the model with the custom admin class
admin.site.register(UserLogin, UserLoginAdmin)
admin.site.register(postUser)
admin.site.register(Discussion)
