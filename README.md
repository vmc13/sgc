# Sistema Gerenciador de Canhotos

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

## Objetivo do projeto
Automatização do processo de conferência de canhotos de notas fiscais
## Requisitos funcionais
- Upload de arquivos CSV
- Visualização, adição, e alteração de dados
- Conferência de dados
- Sistema de autenticação de usuários


## Tecnologias utilizadas
<p display="inline-block">
  <img width="50" src="https://images.vexels.com/media/users/3/166477/isolated/lists/9bb722f0e85ddbc1ce0f064534fd2311-icone-da-linguagem-de-programacao-python.png" alt="logo flutter"/>
  <img width="50" src="https://rathank.com/wp-content/uploads/2022/09/django.png" alt="logo firebase"/>
  <img width="50" src="https://dl2.macupdate.com/images/icons256/63579.png?time=1634203344" alt="logo firebase"/>
  <img width="50" src="https://api.nuget.org/v3-flatcontainer/sqlite.redist/3.8.4.2/icon" alt="logo firebase"/>
</p>

_Python, Django, Git e SqLite (persistência de dados)._

## Acesso e execução
```bash
# Clone este repositório
git clone https://github.com/vmc13/sgc

# Entre na pasta do projeto
cd sgc

# Crie uma virtualenv com Python3
python3 -m venv .venv

# Ative a virtualenv (comando para windows)
.venv/Scripts/Activate

# Instale as dependências
python -m pip install -r requirements.txt

# Gere uma nova SECRET_KEY
python contrib/env_gen.py

# Rode as migrações
python manage.py migrate

# Crie um superusuário para acesso ao sistema
python manage.py createsuperuser

# Inicialize o servidor
python manage.py runserver

# Rota inicial
/auth/login
```

## Referências 
- [python-decouple](https://pypi.org/project/python-decouple/)
- [django-forms-tutorial](https://github.com/rg3915/django-forms-tutorial/blob/main/passo-a-passo.md)
- [django-basic](https://github.com/rg3915/tutoriais/tree/master/django-basic)
- [django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/)
- [Class Based Views](https://ccbv.co.uk/)
- [form-inline](https://felipefrizzo.github.io/post/form-inline/)
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/)
