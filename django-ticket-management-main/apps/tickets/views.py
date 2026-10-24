from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import TicketForm, TicketUpdateForm
from tickets.models import Ticket


class TicketListView(LoginRequiredMixin, ListView):
	model = Ticket
	template_name = 'tickets/ticket_list.html'
	context_object_name = 'tickets'

	def get_queryset(self):
		if self.request.user.role == 'employe':
			return Ticket.objects.filter(cree_par=self.request.user)
		return Ticket.objects.all()


class TicketCreateView(LoginRequiredMixin, CreateView):
	model = Ticket
	form_class = TicketForm
	template_name = 'tickets/ticket_form.html'
	success_url = reverse_lazy('ticket_list')

	def form_valid(self, form):
		form.instance.cree_par = self.request.user
		return super().form_valid(form)


class TicketDetailView(LoginRequiredMixin, UpdateView):
	model = Ticket
	form_class = TicketUpdateForm
	template_name = 'tickets/ticket_detail.html'
	success_url = reverse_lazy('ticket_list')
