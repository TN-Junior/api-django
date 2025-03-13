# Use a imagem oficial do Python
FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para o contêiner
COPY requirements.txt .
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta do Django
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
