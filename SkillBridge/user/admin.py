from django.contrib import admin
from django.utils.html import format_html
from .models import User_Profile

@admin.register(User_Profile)
class User_ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user_link', 'role', 'image_preview')
    list_filter = ('role',)
    search_fields = ('full_name', 'user__username', 'user__email')
    readonly_fields = ('image_preview',)
    list_per_page = 20

    fieldsets = (
        ('User Information', {
            'fields': ('user', 'full_name', 'role')
        }),
        ('Profile Media', {
            'fields': ('image', 'image_preview')
        }),
    )

    def user_link(self, obj):
        if obj.user:
            return obj.user.username
        return "-"
    user_link.short_description = 'User (Username)'
    user_link.admin_order_field = 'user__username'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;" />', obj.image.url)
        return format_html('<span style="color: #999;">{}</span>', 'No Image')
    image_preview.short_description = 'Profile Image'
