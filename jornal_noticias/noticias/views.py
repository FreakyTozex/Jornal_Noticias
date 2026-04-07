from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario


def lista_artigos(request):
    """Página pública que lista o título de todos os artigos."""
    artigos = Artigo.objects.all()
    return render(request, 'news/lista_artigos.html', {'artigos': artigos})


def detalhe_artigo(request, artigo_id):
    """Página pública onde o utilizador pode ver o artigo individual."""
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    return render(request, 'news/detalhe_artigo.html', {'artigo': artigo})


def comentarios_artigo(request, artigo_id):
    """Página pública para ver e publicar comentários de um artigo."""
    artigo = get_object_or_404(Artigo, pk=artigo_id)

    if request.method == 'POST':
        texto = request.POST.get('texto', '').strip()
        if texto:
            Comentario.objects.create(artigo=artigo, texto=texto)
        return redirect('comentarios_artigo', artigo_id=artigo_id)

    comentarios = artigo.comentarios.all()
    return render(request, 'news/comentarios_artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
    })
