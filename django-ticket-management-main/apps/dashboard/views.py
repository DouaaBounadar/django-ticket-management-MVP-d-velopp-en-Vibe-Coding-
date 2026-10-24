from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from tickets.models import Ticket


class DashboardView(LoginRequiredMixin, TemplateView):
	template_name = 'dashboard/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['total_tickets'] = Ticket.objects.count()
		context['tickets_nouvelles'] = Ticket.objects.filter(
			statut=Ticket.STATUT_NOUVELLE,
		).count()
		context['tickets_en_cours'] = Ticket.objects.filter(
			statut=Ticket.STATUT_EN_COURS,
		).count()
		context['tickets_resolues'] = Ticket.objects.filter(
			statut=Ticket.STATUT_RESOLUE,
		).count()
		return context
