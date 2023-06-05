-- Criar usuários
CREATE ROLE usuario;
CREATE ROLE dev;
CREATE ROLE dba;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO usuario;
GRANT SELECT, INSERT, DELETE, UPDATE ON ALL TABLES IN SCHEMA public TO dev;
GRANT ALL ON DATABASE "IGDB" TO dba;

CREATE USER martinsDBA WITH PASSWORD 'fabosmati';
CREATE USER martinsDEV WITH PASSWORD 'fabosmati';
CREATE USER martinsUSER WITH PASSWORD 'fabosmati';

GRANT usuario TO martinsUSER;
GRANT dev TO martinsDEV;
GRANT dba TO martinsDBA;

GRANT USAGE ON SCHEMA public TO martinsUSER;
GRANT USAGE ON SCHEMA public TO martinsDEV;
GRANT USAGE ON SCHEMA public TO martinsDBA;

-- Verificar criação correta de roles e users
SELECT * FROM pg_roles where rolname = 'dev';
SELECT * FROM information_schema.role_table_grants where grantee='usuario';


CREATE TABLE plataform(
    id smallint PRIMARY KEY NOT NULL,
    name varchar(100) NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    abbreviation varchar(50),
    alternative_name varchar(100),
    generation smallint
);

CREATE TABLE genres(
	id smallint PRIMARY KEY NOT NULL,
	name varchar(100) UNIQUE NOT NULL,
	url text NOT NULL,
	created_at date NOT NULL,
	updated_at date NOT NULL
);

CREATE TABLE games_modes(
    id smallint PRIMARY KEY NOT NULL,
    name varchar(40) UNIQUE NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    url text NOT NULL
);

CREATE TABLE companies(
    id int PRIMARY KEY NOT NULL,
    name text NOT NULL,
    country text,
    created_at date NOT NULL,
	updated_at date NOT NULL
);

CREATE TABLE games(
    id int PRIMARY KEY NOT NULL,
    name text NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    url text NOT NULL,
    summary text,
    game_engines text,
    follows int,
    release_date date
);
                            
CREATE TABLE character(
    id int PRIMARY KEY NOT NULL,
    name text NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    url text NOT NULL
);

CREATE TABLE game_plataform(
    id_game int NOT NULL,
    id_plataform smallint NOT NULL,
    FOREIGN KEY (id_game) REFERENCES games(id),
    FOREIGN KEY (id_plataform) REFERENCES plataform(id)
);

CREATE TABLE game_company(
    id_game int NOT NULL,
    id_company int NOT NULL,
    FOREIGN KEY (id_game) REFERENCES games(id),
    FOREIGN KEY (id_company) REFERENCES companies(id)
);

CREATE TABLE game_genre(
    id_game int NOT NULL,
    id_genre smallint NOT NULL,
    FOREIGN KEY (id_game) REFERENCES games(id),
    FOREIGN KEY (id_genre) REFERENCES genres(id)
);

CREATE TABLE game_character(
    id_game int NOT NULL,
    id_character int NOT NULL,  
    FOREIGN KEY (id_game) REFERENCES games(id),
    FOREIGN KEY (id_character) REFERENCES character(id)
);

CREATE TABLE game_gamemode(
    id_game int NOT NULL, 
    id_game_mode smallint NOT NULL,
    FOREIGN KEY (id_game) REFERENCES games(id),
    FOREIGN KEY (id_game_mode) REFERENCES games_modes(id)
);
