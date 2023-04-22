-- Create a table in a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
  id NOT NULL AUTO_INCREMENT,
  name VARCHAR(256),
  PRIMARY KEY (id),
  UNIQUE (id)
);
