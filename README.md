# Jornal_Noticias
## Como utilizar:
    -criar virtual environment (ex: python -m venv virtualenv);
    - entrar no virtualenv (ex: source virtualenv/Scripts/activate);
    - instalar dependencias (pip install -r requirements.txt);
    - aplicar migrações (python manage.py migrate);
    - criar user admin (python manage.py createsuperuser);
    - iniciar servidor (python manage.py runserver)

## Uma vez iniciado o servidor
    - Entrar no link http://localhost:8000/admin e inserir credenciais do superuser;
    - Dentro do painel de admin podes inserir noticias e comentarios para a pagina principal do jornal de noticias;
    - Entrar no Jornal de noticias http://localhost:8000/noticias;
    - Dentro do Jornal podes ver as noticias criadas pelo admin, ver comentários e adicionar comentários a uma noticia especifica.

# Utilização de AI neste projeto
Inteligência Artificial foi utilizada para fix em bugs, um models.py melhor construído e para os templates. O restante do projeto foi desenvolvido por mim com documentação do django e tutoriais na internet :p.
