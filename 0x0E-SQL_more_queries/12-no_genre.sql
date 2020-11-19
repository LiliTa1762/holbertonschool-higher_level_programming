-- Lists all shows contained in hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows 
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY 
	tv_shows.title ASC,
 	tv_show_genres.genre_id ASC;
