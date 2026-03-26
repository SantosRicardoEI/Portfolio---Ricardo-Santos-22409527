# Django — comandos

## 1. Criação inicial do projecto

### 1.1 Criar e activar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 1.2 Instalar o Django

```bash
python -m pip install --upgrade pip
python -m pip install django
```

### 1.3 Criar o projecto Django

```bash
django-admin startproject core .
```

### 1.4 Aplicar as migrations iniciais

```bash
python manage.py migrate
```

### 1.5 Criar o superutilizador

```bash
python manage.py createsuperuser
```

### 1.6 Criar uma app nova

```bash
python manage.py startapp nome_da_app
```

### 1.7 Adicionar a app ao `INSTALLED_APPS`

No ficheiro `core/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'nome_da_app',
]
```

### 1.8 Correr o servidor

```bash
python manage.py runserver
```

---

## 2. Sequência completa de criação do projecto

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install django
django-admin startproject core .
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp nome_da_app
```

Depois disso, adicionar a app ao `INSTALLED_APPS` em `core/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'nome_da_app',
]
```

E por fim:

```bash
python manage.py runserver
```

---

## 3. Comandos normais de manutenção

### Correr o servidor

```bash
python manage.py runserver
```

### Criar uma nova app

```bash
python manage.py startapp nome_da_app
```

### Criar migrations depois de alterar models

```bash
python manage.py makemigrations
```

### Aplicar migrations

```bash
python manage.py migrate
```

### Criar superutilizador

```bash
python manage.py createsuperuser
```

### Abrir a shell do Django

```bash
python manage.py shell
```

### Correr testes

```bash
python manage.py test
```

### Ver migrations

```bash
python manage.py showmigrations
```

### Mudar a password de um utilizador

```bash
python manage.py changepassword nome_do_utilizador
```

---

## 4. Fluxo normal quando crias ou alteras models

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 5. Ambiente virtual

### Activar

```bash
source .venv/bin/activate
```

### Sair

```bash
deactivate
```

---

## 6. Nota importante

O comando:

```bash
python manage.py makemigrations
```

não é necessário logo após criar um projecto Django vazio.

Só deves usá-lo quando criares ou alterares ficheiros `models.py` nas tuas apps.
