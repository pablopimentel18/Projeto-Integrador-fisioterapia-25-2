# Step 1: Base image
FROM python:3.10-slim

# Step 2: Env vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Workdir
WORKDIR /app

# Step 4: System Dependencies (MUDANÇA IMPORTANTE)
# Devemos instalar as dependências do sistema ANTES do pip.
# Se algum pacote no requirements.txt precisar do Pango/Glib para compilar,
# ele falharia na sua versão original.
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libgobject-2.0-0 \
    libglib2.0-dev \
    # Adicione build-essential e libpq-dev se usar Postgres ou precisar compilar C
    # build-essential \
    # libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 5: Python Dependencies
# Boa prática: atualizar o pip antes de instalar os pacotes
RUN pip install --upgrade pip

COPY requirements.txt .

# Adicionado --no-cache-dir para manter a imagem leve
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy project files
COPY . .

# Step 7: Expose port
EXPOSE 8000

# Step 8: Run command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]