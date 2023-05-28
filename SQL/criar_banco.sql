CREATE TABLE plataform(
    id smallint PRIMARY KEY NOT NULL,
    name varchar(100) NOT NULL,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    abbreviation varchar(50),
    alternative_name varchar(100),
    generation smallint
);

CREATE TABLE plataform_version(
    id smallint PRIMARY KEY NOT NULL,
    name varchar(100) NOT NULL,
    os varchar(100),
    memory varchar(30),
    cpu varchar(50),
    graphics varchar(50),
    sound varchar(100),
    connectivity varchar(100),
    resolution varchar(80),
    plataform smallint,
    FOREIGN KEY (plataform) REFERENCES plataform(id)
);

CREATE TABLE genres(
	id smallint PRIMARY KEY NOT NULL,
	name varchar(100) NOT NULL,
	url text NOT NULL,
	created_at date NOT NULL,
	updated_at date NOT NULL
);

CREATE TABLE companies(
    id int PRIMARY KEY NOT NULL,
    name text NOT NULL,
    country varchar(40),
    created_at date NOT NULL,
	updated_at date NOT NULL
);