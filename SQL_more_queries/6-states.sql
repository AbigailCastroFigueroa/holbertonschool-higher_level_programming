-- Create a table in a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS 'htbn_0d_usa'.'states' (
  id NOT NULL UNIQUE AUTO_INCREMENT,
  name VARCHAR(256),
  PRIMARY KEY (id)
);
