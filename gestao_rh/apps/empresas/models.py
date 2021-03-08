import uuid
from django.db import models


class Empresa(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  nome = models.CharField(max_length=100, help_text="Nome da empresa")

  def __str__(self):
      return self.name

