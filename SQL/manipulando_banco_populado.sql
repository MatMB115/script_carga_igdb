SELECT * FROM companies
CREATE TABLE games(


CREATE TABLE games(
    id int PRIMARY KEY NOT NULL,
    name text NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    url text NOT NULL,
    game_modes text,
    summary text,
    game_engines text,
    follows int,
    release_date date
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
	
CREATE TABLE character(
    id int PRIMARY KEY NOT NULL,
    name text NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    url text NOT NULL
);

CREATE TABLE game_character(
    id_game int NOT NULL,
    id_character int NOT NULL,
    FOREIGN KEY (id_game) REFERENCES games(id),
    FOREIGN KEY (id_character) REFERENCES character(id)
);
SELECT * FROM character WHERE id = 7090
SELECT * FROM games WHERE id = 95080
SELECT * FROM companies
SELECT * FROM games
SELECT * FROM genres
SELECT * FROM plataform
	
DELETE FROM plataform;
DELETE FROM game_company;
DELETE FROM game_genre;
DELETE FROM game_plataform;
DELETE FROM character;
DELETE FROM game_character;
	
	
SELECT * FROM games g JOIN game_character gch ON gch.id_game = g.id
	JOIN character ch ON gch.id_character = ch.id