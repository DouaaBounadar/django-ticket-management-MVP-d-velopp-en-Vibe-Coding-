from django.conf import settings
from django.db import models


class AuditLog(models.Model):
	action = models.CharField(max_length=255)
	utilisateur = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='audit_logs',
	)
	date_action = models.DateTimeField(auto_now_add=True)
