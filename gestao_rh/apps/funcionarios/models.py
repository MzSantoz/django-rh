import uuid
from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

class Funcionario(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  nome = models.CharField(max_length=100)
  user = models.OneToOneField(User, on_delete=models.PROTECT)
  empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
  departamentos = models.ManyToManyField(Departamento)


  def __str__(self):
      return self.nome
      