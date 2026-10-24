from django.urls import path

from .views import TicketCreateView, TicketDetailView, TicketListView

urlpatterns = [
	path('', TicketListView.as_view(), name='ticket_list'),
	path('creer/', TicketCreateView.as_view(), name='ticket_create'),
	path('<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
]
