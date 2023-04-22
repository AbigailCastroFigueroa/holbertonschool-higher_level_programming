-- Creating table with default value not null condition
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT NOT NULL DEFAULT 1,
  name VARCHAR(256)
);

