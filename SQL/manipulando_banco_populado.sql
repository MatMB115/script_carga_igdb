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

-- Manipulações gerais do banco

SELECT * FROM companies
	
SELECT * FROM character WHERE id = 7090
SELECT * FROM games WHERE id = 4848
SELECT * FROM companies
SELECT * FROM games WHERE name ilike 'war%'
SELECT * FROM genres
SELECT * FROM plataform
SELECT * FROM character
SELECT * FROM games_modes
SELECT * FROM game_company
SELECT * FROM game_genre
SELECT * FROM game_plataform
SELECT * FROM game_character
SELECT * FROM game_gamemode
-- GERAL		
SELECT * FROM games g JOIN game_character gch ON gch.id_game = g.id JOIN character ch ON gch.id_character = ch.id
	JOIN game_plataform gp ON gp.id_game = g.id JOIN plataform p ON gp.id_plataform = p.id 
	JOIN game_company gc ON g.id = gc.id_game JOIN companies cp ON gc.id_company = cp.id 
	JOIN game_genre gg ON gg.id_game = g.id JOIN genres gr ON gg.id_genre = gr.id
-- GAME + GENRE + PLAT + GAMEMODE
SELECT * FROM games g JOIN game_plataform gp ON gp.id_game = g.id JOIN plataform p ON gp.id_plataform = p.id 
	JOIN game_genre gg ON gg.id_game = g.id JOIN genres gr ON gg.id_genre = gr.id
	JOIN game_gamemode gms ON gms.id_game = g.id JOIN games_modes gmd ON gms.id_game_mode = gmd.id
-- GAME + GENRE + PLAT
SELECT * FROM games g JOIN game_plataform gp ON gp.id_game = g.id JOIN plataform p ON gp.id_plataform = p.id 
	JOIN game_genre gg ON gg.id_game = g.id JOIN genres gr ON gg.id_genre = gr.id
-- GAME + GENRE
EXPLAIN ANALYZE SELECT * FROM games g JOIN game_genre gg ON gg.id_game = g.id JOIN genres gr ON gg.id_genre = gr.id
-- GAME + PLAT
SELECT * FROM games g JOIN game_plataform gp ON gp.id_game = g.id JOIN plataform p ON gp.id_plataform = p.id
-- GAME + COMPANY
SELECT * FROM games g JOIN game_company gc ON g.id = gc.id_game JOIN companies cp ON gc.id_company = cp.id

-- GAME + GAMEMODE
SELECT * FROM games g JOIN game_gamemode gms ON gms.id_game = g.id JOIN games_modes gmd ON gms.id_game_mode = gmd.id

-- EXPLAIN ANALYZE DAS CONSULTAS

EXPLAIN ANALYZE SELECT * FROM games WHERE release_date > '01/01/2011'
EXPLAIN ANALYZE SELECT * FROM games g JOIN game_plataform gp ON gp.id_game = g.id JOIN plataform p ON gp.id_plataform = p.id 
	JOIN game_genre gg ON gg.id_game = g.id JOIN genres gr ON gg.id_genre = gr.id 

-- VERIFICAR ÍNDICES CRIADOS
SELECT * FROM pg_indexes WHERE tablename = 'game_genre';
	
-- CONSULTAR QUANTIDADE DE LINHAS NA TABELA
SELECT table_name, count_rows(table_name) 
FROM information_schema.tables 
WHERE table_schema NOT IN ('pg_catalog', 'information_schema') 
ORDER by count_rows(table_name) DESC

-- CUIDADO DELETES!!!!!!
DELETE FROM games;
DELETE FROM companies;
DELETE FROM games_modes;
DELETE FROM genres;
DELETE FROM plataform;
DELETE FROM character;
DELETE FROM games_modes;
DELETE FROM game_company;
DELETE FROM game_genre;
DELETE FROM game_plataform;
DELETE FROM game_character;
DELETE FROM game_gamemode;
