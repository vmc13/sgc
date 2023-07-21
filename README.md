# Sistema Gerenciador de Canhotos

## Execução
```bash
# Crie uma virtualenv com Python3
python3 -m venv .venv

# Instale as dependências
python -m pip install -r requirements.txt

# Gere uma nova SECRET_KEY
python contrib/env_gen.py

# Rode as migrações
python manage.py migrate

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
