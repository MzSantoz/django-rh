import uuid
from django.db import models
from apps.funcionarios.models import Funcionario

class Documento(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  descricao = models.CharField(max_length=100)
  proprietario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
  

  def __str__(self):
      return self.descricao
  
