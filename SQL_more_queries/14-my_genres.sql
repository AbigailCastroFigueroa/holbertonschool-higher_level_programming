-- Show related genre from a selected film.
SELECT name FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE title="Dexter"
ORDER BY tv_genres.name ASC;

