from django.db import models

class Pagina(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField(max_length=1200)

    def __str__(self):
        return self.titulo