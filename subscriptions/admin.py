from django.utils.timezone import now
from django.contrib import admin
from subscriptions.models import Subscription

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'subscribe_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)

    def subscribe_today(self, obj):
        return obj.created_at == now().date()

    subscribe_today.short_description = 'inscrito hoje?'
    subscribe_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
