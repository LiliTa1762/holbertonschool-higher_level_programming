-- Lists all shows contained in hbtn_0d_tvshows
-- The show_id of tv_show_genre are the same of the  id of tv_show
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows 
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY 
	tv_shows.title ASC,
 	tv_show_genres.genre_id ASC;
