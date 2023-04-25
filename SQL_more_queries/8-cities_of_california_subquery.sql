-- Select fields co-related between two different tables.
SELECT id, state_id, name FROM cities WHERE EXISTS (SELECT id FROM states WHERE cities.state_id = states.id AND states.name = 'California') ORDER BY cities.id ASC;

