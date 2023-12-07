# Lacrei Saúde Backend

Esta API tem como objetivo possibilitar a criação, edição e exclusão de profissionais e consultas. Foi utilizado o Django Rest Framework.

## Configurando ambiente

Comece fazendo o clone deste repositório:
```bash
git clone https://github.com/alimarques/lacrei-saude-backend.git
```

Para que não haja conflito de pacotes, crie e ative uma `venv`:
```bash
python3 -m venv venv
source venv/bin/activate
```

Instale os pacotes python que são necessários:
```bash
pip install -r requirements.txt
```

Em seguida migre os modelos:
```bash
python manage.py migrate
```

Por fim, rode a aplicação localmente:
```bash
python manage.py runserver
```

## Funcionamento da API

A aplicação foi realizada por meio do Django Rest Framework pela facilidade de configuração do CRUD. Os modelos foram definidos conforme instruções dos requisitos. 

Há duas formas de fazer as requisições para a API: Pela interface disponível em http://127.0.0.1:8000/lacreisaude/v1/ ou pelo Postman. Abaixo descrevo os passos para testar no Postman. Não configurei nenhuma autenticação para ser mais rápido testar (nas views, foi setada a opção `permission_classes = [permissions.AllowAny]`).

### Profissionais

Retornar todas as pessoas profissionais:
```
GET http://127.0.0.1:8000/lacreisaude/v1/profissionais
```

Retornar uma pessoa profissional específica:
```
GET http://127.0.0.1:8000/lacreisaude/v1/profissionais/{id_profissional}
```

Cadastrar uma pessoa profissional:
```
POST http://127.0.0.1:8000/lacreisaude/v1/profissionais
body = {
    "nome_social": "Maria da Silva"
}
```

Atualizar uma pessoa profissional:
```
PUT http://127.0.0.1:8000/lacreisaude/v1/profissionais/{id_profissional}
body = {
    "nome_social": "Maria de Souza"
}
```

Deletar uma pessoa profissional:
```
DELETE http://127.0.0.1:8000/lacreisaude/v1/profissionais/{id_profissional}
```

### Consultas

Retornar todas as consultas:
```
GET http://127.0.0.1:8000/lacreisaude/v1/consultas
```

Retornar uma consulta específica:
```
GET http://127.0.0.1:8000/lacreisaude/v1/consultas/{id_consulta}
```

Cadastrar uma consulta:
```
POST http://127.0.0.1:8000/lacreisaude/v1/consultas
body = {
    "data_consulta": "2024-02-12T08:30:00Z",
    "profissional": 1
}
```
Obs.: A pessoa profissional deve existir para que seja feita a associação.

Atualizar uma consulta:
```
PUT http://127.0.0.1:8000/lacreisaude/v1/consultas/{id_consulta}
body = {
    "data_consulta": "2024-01-05T08:00:00Z"
}
```

Deletar uma consulta:
```
DELETE http://127.0.0.1:8000/lacreisaude/v1/consultas/{id_consulta}
```

Retornar todas as consultas de uma pessoa profissional:
```
GET http://127.0.0.1:8000/lacreisaude/v1/consultas?profissional={id_profissional}
```

## Testes

Alguns testes unitários foram feitos:
- Assegurar comportamento de GET e POST das views;
- Assegurar campos dos modelos;
- Assegurar consistência de chaves estrangeiras.

Para rodar os testes:
```bash
python manage.py test
```

## TO DO

- [ ] Criação de modelo para pessoa que está marcando a consulta;
- [ ] Trazer mais informações como local da consulta, especialidade, etc;
- [ ] Bloquear criação de consultas que ocorrem ao mesmo tempo para uma pessoa profissional;
- [ ] Definir intervalos disponíveis para marcar consulta com pessoa profissional.