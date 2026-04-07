from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # Adicionar campo autor ao Artigo
        migrations.AddField(
            model_name='artigo',
            name='autor',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='artigos',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        # Adicionar campo nome_autor ao Comentario
        migrations.AddField(
            model_name='comentario',
            name='nome_autor',
            field=models.CharField(default='Anónimo', max_length=100),
            preserve_default=False,
        ),
    ]