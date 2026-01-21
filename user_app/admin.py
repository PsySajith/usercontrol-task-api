from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# remove default registration
admin.site.unregister(User)

# register again with custom admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'email')



# "User model already has a built-in admin class.
# We extend UserAdmin instead of ModelAdmin
# so we don’t lose default authentication features."