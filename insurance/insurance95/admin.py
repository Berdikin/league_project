from django.contrib import admin

# Register your models here.

from .models import *


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'surname', 'name', 'patronymic', 'entity', 'photo')
    list_display_links = ('client_id', 'surname', 'name', 'patronymic')
    search_fields = ('surname', 'name', 'patronymic')
    list_filter = ('entity', )


class PassportDateAdmin(admin.ModelAdmin):
    list_display = ('passport_id', 'surname', 'name', 'patronymic', 'date_birth', 'series', 'number')
    list_display_links = ('passport_id', 'surname', 'name', 'patronymic')
    search_fields = ('surname', 'name', 'patronymic')


class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('insurance_id', 'client_id', 'region_id', 'max_payment', 'cost', 'type',
                    'date_conclusion_contract', 'period_start_date',
                    'period_end_date')
    list_display_links = ('insurance_id', 'client_id')
    search_fields = ()
    list_filter = ('region_id', 'type', 'date_conclusion_contract', 'period_start_date', 'period_end_date')


class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_id', 'region_name')
    list_display_links = ('region_id', 'region_name')
    search_fields = ('region_name',)


class TypeInsuranceAdmin(admin.ModelAdmin):
    list_display = ('type_id', 'type_name')
    list_display_links = ('type_id', 'type_name')
    search_fields = ('type_name',)


#admin.site.register(admins)

admin.site.register(agent)

admin.site.register(region, RegionAdmin)

admin.site.register(insurance, InsuranceAdmin)

admin.site.register(type_insurance, TypeInsuranceAdmin)

admin.site.register(additional_service)

admin.site.register(type_service)

admin.site.register(passport_date, PassportDateAdmin)

admin.site.register(clients, ClientsAdmin)
