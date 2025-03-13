# **API Django - Taxa Selic**

## **Visão Geral**
Este projeto é uma API desenvolvida em Django para buscar e armazenar as taxas Selic em um banco de dados MySQL. A aplicação utiliza **Docker** e **Docker Compose** para facilitar a configuração e execução do ambiente, garantindo portabilidade e escalabilidade.

A API permite a recuperação das taxas Selic a partir de uma fonte externa e armazena os dados no banco para consultas futuras.

---

## ⚙️ **Configuração e Instalação**

### **1️⃣ Pré-requisitos**
Antes de iniciar, certifique-se de ter instalado:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)

---

### **2️⃣ Clonar o repositório**
Para obter o código-fonte do projeto, execute:

```sh
git clone https://github.com/TN-Junior/api-django.git

cd desafio_python # arquivos de configuração do django
cd selic # arquivo coma lógica de extração de dados da api
```

### **3️⃣ Configurar as variáveis de ambiente**
Crie um arquivo .env (se necessário) ou edite o settings.py para garantir que as credenciais do banco de dados estejam corretas.

Exemplo de configuração do banco de dados (settings.py):
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'django_user',
        'PASSWORD': 'django_password',
        'HOST': 'db',  
        'PORT': '3306',
    }
}
```
## **Executando o Projeto**
### **1️⃣ Subir os containers Docker**
Para iniciar o banco de dados e o Django dentro do ambiente Docker, rode:
```sh
docker-compose up -d
```
Isso iniciará os serviços:

- db: Banco de dados MySQL

- web: Aplicação Django

### **2️⃣ Aplicar migrações do banco**
Após iniciar os containers, aplique as migrações para criar as tabelas no MySQL:
```sh
docker-compose exec web python manage.py migrate
```
Se necessário, crie um superusuário para acessar o Django Admin:
```sh
docker-compose exec web python manage.py createsuperuser
```

### **3️⃣ Coletar dados da API**
Para buscar as taxas Selic e armazená-las no banco de dados, execute:
```sh
docker-compose exec web python manage.py fetch_selic
```

### **4️⃣ Rodar o servidor Django**
Agora, inicie o servidor da API:
```sh
docker-compose exec web python manage.py runserver 0.0.0.0:8000
```
Acesse a API no navegador:
http://localhost:8000

## Comandos úteis
Se precisar parar os containers:
```sh
docker-compose down
```
Para limpar os volumes (⚠️ Isso apagará os dados do banco):
```sh
docker-compose down -v
```
