from django.contrib import admin
from django import forms
from django.utils import timezone
from .models import Buku, Agenda, Dokumentasi


class AgendaAdminForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tanggal'].widget.attrs['min'] = timezone.localdate().isoformat()


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    form = AgendaAdminForm
    list_display = ('nama_agenda', 'tanggal')
    ordering = ('-tanggal',)


admin.site.register(Buku)
admin.site.register(Dokumentasi)
