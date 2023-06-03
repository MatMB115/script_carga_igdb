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
SELECT * FROM games WHERE id = 4848
SELECT * FROM companies
SELECT * FROM games
SELECT * FROM genres
SELECT * FROM plataform
SELECT * FROM character
SELECT * FROM game_company
SELECT * FROM game_genre
SELECT * FROM game_plataform
SELECT * FROM game_character
-- GERAL		
SELECT * FROM games g JOIN game_character gch ON gch.id_game = g.id JOIN character ch ON gch.id_character = ch.id 
	JOIN game_plataform gp ON gp.id_game = g.id JOIN plataform p ON gp.id_plataform = p.id 
	JOIN game_company gc ON g.id = gc.id_game JOIN companies cp ON gc.id_company = cp.id 
	JOIN game_genre gg ON gg.id_game = g.id JOIN genres gr ON gg.id_genre = gr.id
-- GAME + GENRE + PLAT
SELECT * FROM games g JOIN game_plataform gp ON gp.id_game = g.id JOIN plataform p ON gp.id_plataform = p.id 
	JOIN game_genre gg ON gg.id_game = g.id JOIN genres gr ON gg.id_genre = gr.id
-- GAME + GENRE
SELECT * FROM games g JOIN game_genre gg ON gg.id_game = g.id JOIN genres gr ON gg.id_genre = gr.id
-- GAME + PLAT
SELECT * FROM games g JOIN game_plataform gp ON gp.id_game = g.id JOIN plataform p ON gp.id_plataform = p.id
-- GAME + COMPANY
SELECT * FROM games g JOIN game_company gc ON g.id = gc.id_game JOIN companies cp ON gc.id_company = cp.id
	
-- CUIDADO DELETES!!!!!!
DELETE FROM plataform;
DELETE FROM game_company;
DELETE FROM game_genre;
DELETE FROM game_plataform;
DELETE FROM character;
DELETE FROM games;
