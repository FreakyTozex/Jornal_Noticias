from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Artigo, Comentario


def lista_artigos(request):
    query = request.GET.get('q', '').strip()
    artigos = Artigo.objects.select_related('autor')

    if query:
        artigos = artigos.filter(
            Q(titulo__icontains=query) | Q(corpo__icontains=query)
        )

    return render(request, 'news/lista_artigos.html', {
        'artigos': artigos,
        'query': query,
    })


def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo.objects.select_related('autor'), pk=artigo_id)
    return render(request, 'news/detalhe_artigo.html', {'artigo': artigo})


def comentarios_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)

    errors = {}

    if request.method == 'POST':
        nome_autor = request.POST.get('nome_autor', '').strip()
        texto = request.POST.get('texto', '').strip()

        if not nome_autor:
            errors['nome_autor'] = 'O nome é obrigatório.'
        if not texto:
            errors['texto'] = 'O comentário não pode estar vazio.'

        if not errors:
            Comentario.objects.create(artigo=artigo, nome_autor=nome_autor, texto=texto)
            return redirect('comentarios_artigo', artigo_id=artigo_id)

    comentarios = artigo.comentarios.all()
    return render(request, 'news/comentarios_artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'errors': errors,
        'post_data': request.POST,
    })