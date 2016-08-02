# coding=utf-8
from django.contrib import admin
from .models import Ticket, Setup
from django.forms import ModelForm
from suit.widgets import EnclosedInput, AutosizedTextarea


class SetupAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email')

    def has_add_permission(self, request):
        if Setup.objects.count() == 0:
            return True
        else:
            return False


class TicketAdminForm(ModelForm):
    class Meta:
        widgets = {
            'comment': AutosizedTextarea,
        }


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created', 'status', 'manager')
    list_filter = ['created', 'status', 'manager', 'contact_date']
    search_fields = ['manager',]
    date_hierarchy = 'created'
    fields = ('name', 'phone', 'country', 'city', 'time_zone', 'status', 'contact_date', 'manager', 'comment', 'sale')
    form = TicketAdminForm

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            qs = Ticket.objects.filter(sale=False)
        else:
            qs = Ticket.objects.filter(manager=user, sale=False)
        return qs


class Sale(Ticket):
    class Meta:
        proxy = True
        verbose_name = u'Продажа'
        verbose_name_plural = u'Продажи'
        app_label = 'landing'


class SaleAdminForm(ModelForm):
    class Meta:
        widgets = {
            'price': EnclosedInput(append=u'руб.'),
            'comment': AutosizedTextarea,
        }


class SaleAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            return self.model.objects.filter(sale=True)
        else:
            return self.model.objects.filter(manager=user, sale=True)

    def has_add_permission(self, request, obj=None):
        return False

    list_display = ('name', 'phone', 'created', 'price')
    list_filter = ['created', 'status', 'manager']
    date_hierarchy = 'created'
    fields = ('name', 'phone', 'country', 'city', 'time_zone', 'manager', 'comment', 'price')
    form = SaleAdminForm


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Setup, SetupAdmin)
