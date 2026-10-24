from django import forms

from tickets.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titre', 'description']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['statut', 'assigne_a']
        widgets = {
            'statut': forms.Select(attrs={'class': 'form-select'}),
            'assigne_a': forms.Select(attrs={'class': 'form-select'}),
        }
