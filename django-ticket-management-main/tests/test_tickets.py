from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from tickets.models import Ticket


class TicketViewTests(TestCase):
    password = 'Strong-test-password-2026!'

    def create_user(self, email, role='employe'):
        return CustomUser.objects.create_user(
            email=email,
            password=self.password,
            role=role,
        )

    def create_ticket(self, creator, title):
        return Ticket.objects.create(
            titre=title,
            description=f'Description for {title}',
            cree_par=creator,
        )

    def test_ticket_creation(self):
        employee = self.create_user('employee@example.com')
        self.assertTrue(
            self.client.login(
                username=employee.email,
                password=self.password,
            )
        )

        response = self.client.post(
            reverse('ticket_create'),
            {
                'titre': 'Accès VPN',
                'description': 'Impossible de se connecter au VPN.',
            },
        )

        self.assertRedirects(response, reverse('ticket_list'))
        ticket = Ticket.objects.get(titre='Accès VPN')
        self.assertEqual(ticket.cree_par, employee)

    def test_employe_ticket_isolation(self):
        employee_a = self.create_user('employee-a@example.com')
        employee_b = self.create_user('employee-b@example.com')
        self.create_ticket(employee_a, 'Ticket visible pour A')
        self.create_ticket(employee_b, 'Ticket privé pour B')
        self.assertTrue(
            self.client.login(
                username=employee_a.email,
                password=self.password,
            )
        )

        response = self.client.get(reverse('ticket_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ticket visible pour A')
        self.assertNotContains(response, 'Ticket privé pour B')

    def test_technicien_sees_all_tickets(self):
        employee_a = self.create_user('employee-a@example.com')
        employee_b = self.create_user('employee-b@example.com')
        self.create_ticket(employee_a, 'Ticket de A')
        self.create_ticket(employee_b, 'Ticket de B')
        technician = self.create_user('technician@example.com', role='technicien')
        self.assertTrue(
            self.client.login(
                username=technician.email,
                password=self.password,
            )
        )

        response = self.client.get(reverse('ticket_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ticket de A')
        self.assertContains(response, 'Ticket de B')
