
# Logs Management API

## Descrição
Este projeto implementa uma API em Flask para o gerenciamento de logs, utilizando Redis inicialmente para o armazenamento temporário de dados e, posteriormente, transferindo-os para um banco de dados relacional. O uso do Redis como cache visa otimizar a performance da API, especialmente útil em cenários de alta demanda de escrita de logs. Este projeto é um estudo relacionado ao uso de cache em APIs e gerenciamento eficiente de logs.

## Funcionalidades
- **Postar Logs**: Permite o envio de mensagens de log com tags associadas.
- **Consultar Logs**: Oferece a possibilidade de consultar logs específicos por ID, todos os logs, ou logs por tag.
- **Contar Logs por Tag**: Retorna a quantidade de logs associados a uma tag específica.

## Tecnologias Utilizadas
- **Flask**: Framework web usado para construir a API.
- **Redis**: Utilizado como sistema de armazenamento em cache.
- **SQLAlchemy**: Utilizando como ORM para interação com o banco de dados
- **SQL (Banco de Dados Relacional)**: Utilizado para armazenamento permanente de logs.

## Como Usar

### Pré-Requisitos
Antes de iniciar, certifique-se de ter instalado:
- Python 3.6+
- Flask
- Redis
- SQLAlchemy
- Um cliente SQL compatível com sua base de dados relacional

### Configuração
1. Clone o repositório do projeto:
   ```bash
   git clone https://github.com/maxsonferovante/LogsManagement.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure o acesso ao Redis e ao banco de dados relacional no arquivo de configuração da aplicação.

### Inicializando a API
Execute o seguinte comando para iniciar o servidor Flask:
```bash
flask run
```

### Endpoints Disponíveis

#### POST /logs
- **Descrição**: Registra um novo log.
- **Parâmetros**: `name` (query) - Nome da aplicação que envia o log.
- **Payload**:
  ```json
  {
    "log": "Mensagem do log",
    "tag": "DEBUG"
  }
  ```
- **Exemplo de Uso**:
  ```bash
  curl -X POST http://127.0.0.1:8000/logs?name=app -H "Content-Type: application/json" -d '{"log": "This is a log message", "tag": "DEBUG"}'
  ```

#### GET /logs/{id}
- **Descrição**: Busca um log por seu ID.
- **Exemplo de Uso**:
  ```bash
  curl http://127.0.0.1:8000/logs/2624 -H "Accept: application/json"
  ```

#### GET /logs/all
- **Descrição**: Retorna todos os logs armazenados.
- **Exemplo de Uso**:
  ```bash
  curl http://127.0.0.1:8000/logs/all -H "Accept: application/json"
  ```

#### GET /logs/tags/available
- **Descrição**: Lista todas as tags disponíveis.
- **Exemplo de Uso**:
  ```bash
  curl http://127.0.0.1:8000/logs/tags/available -H "Accept: application/json"
  ```

#### GET /logs/tag/{tag}/count
- **Descrição**: Conta quantos logs existem com uma determinada tag.
- **Exemplo de Uso**:
  ```bash
  curl http://127.0.0.1:8000/logs/tag/DEBUG/count -H "Accept: application/json"
  ```

## Contribuições
Contribuições são bem-vindas. Por favor, envie pull requests para melhorar a funcionalidade, corrigir bugs ou sugerir melhorias.

