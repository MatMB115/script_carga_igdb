<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/MatMB115/script_carga_igdb?color=a015f5">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/MatMB115/script_carga_igdb">

  <a href="https://github.com/MatMB115/script_carga_igdb/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/MatMB115/script_carga_igdb">
  </a>
  <a href="https://www.heroku.com/">
  <img alt="Database" src="https://img.shields.io/badge/database PostgreSQL-red">
  </a>

<img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
  <a href="https://github.com/MatMB115/script_carga_igdb/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/MatMB115/script_carga_igdb?style=social">
  </a>
</p>

<p align="center">
  <a href="https://github.com/MatMB115/script_carga_igdb">
    <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*DpaeArqM7JWzJLylsVl9lg.png" height="250" width="500" alt="IGDB-logo" />
  </a>
</p>

<p align="center">
    <a href="https://www.python.org/">
        <img align="center" alt="Python" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg">
    </a>
</p>

# Script de carga para API do IGDB

Script em python formulado para realizar a carga no banco de dados relacional com PostgreSQL e utilizando ORM SQLAlchemy.

---
## Sobre

Conforme as orientações para realização da parte 1 do trabalho da disciplina de Banco de Dados II da Universidade Federal de Itajubá, a equipe desenvolveu um script responsável por realizar a carga nas tabelas do banco. O MER utilizado está presente na Figura abaixo e os códigos SQL para criação do banco na pasta [SQL](./SQL/).

As orientações estão divididas nos seguintes tópicos:

- [Script de carga para API do IGDB](#script-de-carga-para-api-do-igdb)
  - [Sobre](#sobre)
  - [To Do :gear:](#to-do-gear)
  - [Banco de dados :chair: :game\_die:](#banco-de-dados-chair-game_die)
  - [Pré-requisitos e configuração :hammer\_and\_wrench:](#pré-requisitos-e-configuração-hammer_and_wrench)
  - [Tecnologias :technologist:](#tecnologias-technologist)
  - [Contribuidores](#contribuidores)

---
## To Do :gear:
- [x] Etapa 1
  - [x] Escolher API
- [x] Etapa 2
  - [x] Estudar os Dados da API
  - [x] Gerar Modelo Entidade Relacionamento
  - [x] Implementar Banco de Dados
- [x] Etapa 3
  - [x] Criar script
  - [x] Inserir Plataformas
  - [x] Inserir Gêneros
  - [x] Inserir Companhias
  - [x] Inserir Modos de Jogo
  - [x] Inserir Jogos
  - [x] Inserir Personagens
  - [x] Criar índices
    - [x] Data de Lançamento Jogos
    - [x] Relacionamento Plataforma e Games
    - [x] Relacionamento Gênero e Games
    - [x] Relacionamneto Modo de Jogo e Games
  - [x] Funções
    - [x] Count das tabelas
- [x] Etapa 4
  - [x] Testar com JMeter
  - [x] Documentação da parte um
  - [x] Vídeo explicativo

---
## Banco de dados :chair: :game_die:
A aplicação utiliza um banco relacional presente no modelo entidade relacionamento abaixo:
![MER_IGDB](./Docs/MER_GAMES.png)

Para realizar a conexão com o banco utilizou-se:
>PostgreSQL - 15.2

>PGadmin4 - 7.2

>SQLAlchemy - 1.4.48

Ademais, o grupo também disponibilizou backups do banco conforme a quantidade de dados inseridos na pasta [Backups](./SQL/backups_banco/).
Os backups disponíveis são:
- [x] 230K de jogos
- [x] 60K de jogos

---
## Pré-requisitos e configuração :hammer_and_wrench:
No geral, para executar a aplicação é recomendado que o sistema já possua:

    > Python 3.11

Para executar esse script é necessário:

```bash

# Criar o banco com nome IGDB para realizar a carga

# Clone este repositório com
$ git clone https://github.com/MatMB115/script_carga_igdb
# OU
$ git clone git@github.com:MatMB115/script_carga_igdb.git

# Navegue até o diretório clonado com terminal

$ cd script_carga_igdb
$ cd script

# Instale as dependências
$ pip install -r reqs.txt

# Abra script no Vscode ou editor de preferência
$ code .

# No DAO, mude as credenciais de acesso do banco (lembre-se de criar um banco com o nome IGDB pelo SGDB)
$ engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/IGDB")

# Rode o script pelo terminal
$ py controller.py
# OU
$ python3 controller.py

# Lembre-se de gerar o Token Twitch (opção 1 do menu) antes de tentar popular as tabelas!
# Há ums ordem correta identificada no menu para popular elas!

```
---
## Tecnologias :technologist:
    O ponto de início deste projeto foi um ambiente Python, as dependências utilizadas estão presentes no 'reqs.txt'. 
---
Dependências:

    -> Python 3.11
    - SQLAlchemy 2.3
    - psycopg2 2.9.6
    - iso3166 2.1.1
    - annotated-types 0.5
    - igdb-api-v4 0.2
    - protobuf 4.23.2
    - sqlacodegen 3.0.0rc2
---
Banco de Dados:

    -> PostgreSQL
    - pgAdmin4 7.0
    - BRmodelo
---
Utilitários:

    -> Dev
    - Visual Studio Code 1.78
---  

## Contribuidores

<table>
  <tr>
</td>
    <td align="center"><a href="https://github.com/MatMB115"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/63670910?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Martins</b></sub></a><br /><a href="https://github.com/MatMB115/repime" title="RepiMe">:technologist:</a></td>
</td>
  </tr>
</table>
