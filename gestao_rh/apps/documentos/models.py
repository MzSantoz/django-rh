import uuid
from django.db import models

class Documento(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  descricao = models.CharField(max_length=100)

  def __str__(self):
      return self.descricao
  
