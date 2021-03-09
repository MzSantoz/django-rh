import uuid
from django.db import models
from apps.funcionarios.models import Funcionario

class RegistroHoraExtra(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  motivo = models.CharField(max_length=100)
  funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

  def __str__(self):
      return self.motivo
  
