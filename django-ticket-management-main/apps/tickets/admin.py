from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	list_display = ('titre', 'statut', 'cree_par', 'assigne_a', 'date_creation')
	list_filter = ('statut',)
