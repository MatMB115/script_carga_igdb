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

Conforme as orientações para realização da parte 1 do trabalho da disciplina de Banco de Dados II da Universidade Federal de Itajubá, a equipe desenvolveu um script responsável por realizar a carga nas tabelas do banco. O MER utilizado está presente na Figura abaixo e os códigos SQL para criação do banco na pasta [SQL](https://github.com/MatMB115/script_carga_igdb/blob/main/SQL).

As orientações estão divididas nos seguintes tópicos:

- [Script de carga para API do IGDB](#script-de-carga-para-api-do-igdb)
  - [Sobre](#sobre)
  - [Funcionalidades :gear:](#funcionalidades-gear)
  - [Banco de dados :chair: :game\_die:](#banco-de-dados-chair-game_die)
  - [Pré-requisitos e configuração :hammer\_and\_wrench:](#pré-requisitos-e-configuração-hammer_and_wrench)
  - [Tecnologias :technologist:](#tecnologias-technologist)
  - [Contribuidores](#contribuidores)

---
## Funcionalidades :gear:

 - [x] Inserir plataformas;
 - [x] Inserir gêneros;
 - [x] Inserir companhias;
 - [ ] Permitir o anúncio de novas vagas para usuários cadastrados;
 - [ ] Marcar no mapa as vagas já cadastradas.

---
## Banco de dados :chair: :game_die:
A aplicação utiliza um banco relacional presente no modelo entidade relacionamento abaixo...

Para realizar a conexão com o banco utilizou-se:
>postgres: 15.2^
>PGadmin4

---
## Pré-requisitos e configuração :hammer_and_wrench:
No geral, para executar a aplicação é recomendado que o sistema já possua:

    > Python 3^;

Para executar esse script é necessário:

```bash

# Clone este repositório com
$ git clone https://github.com/MatMB115/script_carga_igdb
# ou
$ git clone git@github.com:MatMB115/script_carga_igdb.git

# Instale as dependências
$ pip intall {nome_da_dependência}

# Destaque para ISO3166
$ pip install iso3166

# Abra script no Vscode e rode com button run
code .

#Rode o script pelo terminal
$ py controller.py
#ou
$ python3 controller.py


```
---
## Tecnologias :technologist:
    O ponto de início deste projeto foi um ambiente Python, as dependências utilizadas estão presentes no Pipfile. 
---
Dependências:

    -> Python 3.10.10
    - SQLAlchemy 2.3
    - Psycopg2
    - iso3166 2.1.1
    - datetime
---
Banco de Dados:

    -> PostgreSQL
    - pgAdmin4 7.0
    - BRmodelo
---
Utilitários:

    -> Dev
    - Visual Studio Code 1.73
---  

## Contribuidores

<table>
  <tr>
</td>
    <td align="center"><a href="https://github.com/MatMB115"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/63670910?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Martins</b></sub></a><br /><a href="https://github.com/MatMB115/repime" title="RepiMe">:technologist:</a></td>
</td>
  </tr>
</table>
