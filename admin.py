from django.contrib import admin
from .models import Adv
from django.db.models.query import QuerySet

# Register your models here.

class AdvAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction', 'image']
    list_filter = ['auction', 'created_at']
    actions = ['make_action_as_false', 'make_action_as_true']
    fieldsets = (
        ('общие'{
            'fields':(
                'title', 'description'
            ),
        }),
        ('финансы'{
            'fields':(
                'prise', 'auction'
            ),
            'classes'
        }),
    )

    @admin.action(description='убрать торг')
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction=False)

    @admin.action(description='добавить торг')
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction=True)


admin.site.register(Adv, AdvAdmin)

