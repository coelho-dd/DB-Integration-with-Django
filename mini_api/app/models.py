from django.db import models

# Create your models here.
class Pessoa(models.Model):
    PessoaID = models.IntegerField(primary_key=True)
    PrimeiroNome = models.CharField(max_length=255)
    UltimoNome = models.CharField(max_length=255)
    Cidade = models.CharField(max_length=255)
    Estado = models.CharField(max_length=255)
    Idade = models.IntegerField()

    class Meta:
        db_table = 'People'

    