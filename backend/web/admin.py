from django.contrib import admin
from web.models.user import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'role', 'status', 'created_at')
    list_filter = ('role', 'status')
    search_fields = ('user__username', 'user__email', 'phone')
    list_editable = ('role', 'status')
