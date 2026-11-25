from django.contrib import admin
from .models import AccessRequest


@admin.register(AccessRequest)
class AccessRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "resource", "status", "created_at")
    list_filter = ("status",)
    actions = ["approve_selected", "reject_selected"]

    @admin.action(description="Approve selected requests")
    def approve_selected(self, request, queryset):
        for obj in queryset:
            obj.approve()

    @admin.action(description="Reject selected requests")
    def reject_selected(self, request, queryset):
        for obj in queryset:
            obj.reject()