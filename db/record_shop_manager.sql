DROP TABLE IF EXISTS records;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS genres;

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  country VARCHAR(255)
);

CREATE TABLE genres (
  id SERIAL PRIMARY KEY,
  genre_name VARCHAR(255)
);

CREATE TABLE records (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  artist_id INT NOT NULL REFERENCES artists(id),
  genre_id INT NOT NULL REFERENCES genres(id),
  year INT,
  stock_count INT, 
  buying_cost FLOAT,
  price FLOAT
);
