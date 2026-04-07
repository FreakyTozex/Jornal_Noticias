from django.db import models
from django.contrib.auth.models import User


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    corpo = models.TextField()
    autor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='artigos',
    )
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    nome_autor = models.CharField(max_length=100)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['data_publicacao']

    def __str__(self):
        return f'{self.nome_autor} em "{self.artigo.titulo}"'