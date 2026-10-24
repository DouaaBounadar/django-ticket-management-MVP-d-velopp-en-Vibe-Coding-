from django.conf import settings
from django.db import models


class Ticket(models.Model):
	STATUT_NOUVELLE = 'Nouvelle'
	STATUT_EN_COURS = 'En cours'
	STATUT_RESOLUE = 'Résolue'
	STATUT_CHOICES = [
		(STATUT_NOUVELLE, STATUT_NOUVELLE),
		(STATUT_EN_COURS, STATUT_EN_COURS),
		(STATUT_RESOLUE, STATUT_RESOLUE),
	]

	titre = models.CharField(max_length=255)
	description = models.TextField()
	statut = models.CharField(
		max_length=20,
		choices=STATUT_CHOICES,
		default=STATUT_NOUVELLE,
	)
	date_creation = models.DateTimeField(auto_now_add=True)
	cree_par = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='tickets_crees',
	)
	assigne_a = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='tickets_assignes',
	)
