# Utiliser l'image officielle Python
FROM python:3.12.3

# Créer un utilisateur et un groupe 'appuser', et créer un répertoire home
RUN groupadd -r appuser && useradd -r -g appuser -m -d /home/appuser appuser

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers et dossiers nécessaires dans le répertoire de travail
COPY . /app

# Assurer que l'utilisateur appuser est propriétaire des répertoires
RUN chown -R appuser:appuser /app /home/appuser

# Ajouter le répertoire pip local de l'utilisateur au PATH
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Basculer vers l'utilisateur non-root
USER appuser

# Mettre à jour pip sans utiliser de cache
RUN python -m pip install --no-cache-dir --upgrade pip

# Installer les dépendances de l'application sans utiliser de cache
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exposer le port que l'application va utiliser
EXPOSE 8000

# Définir le point d'entrée pour le conteneur (modifié pour être cohérent avec la structure)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




FROM python:3.12.3

RUN groupadd -r appuser && useradd -r -g appuser -m -d /home/appuser appuser

WORKDIR /app

COPY . /app

RUN chown -R appuser:appuser /app /home/appuser

ENV PATH="/home/appuser/.local/bin:${PATH}"

USER appuser

RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "My_blog.wsgi:application"]




FROM python:3.12.3

RUN groupadd -r appuser && useradd -r -g appuser -m -d /home/appuser appuser

WORKDIR /app

COPY . /app

RUN chown -R appuser:appuser /app /home/appuser

ENV PATH="/home/appuser/.local/bin:${PATH}"

USER appuser

RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "My_blog.wsgi:application"]