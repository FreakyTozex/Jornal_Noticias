from django.db import models


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    corpo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['data_publicacao']

    def __str__(self):
        return f'Comentário em "{self.artigo.titulo}" — {self.data_publicacao.strftime("%d/%m/%Y %H:%M")}'
