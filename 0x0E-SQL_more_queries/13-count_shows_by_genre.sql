-- Lists all genres from hbtn_0d_tvshows
-- Displays the number of shows linked to each
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows FULL OUTER JOIN tv_show_genres

ORDER BY 
	tv_shows.title ASC,
 	tv_show_genres.genre_id ASC;
