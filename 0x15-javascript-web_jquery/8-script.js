$.get('https://swapi-api.hbtn.io/api/films/?format=json', data => {
  const movies = data.results;
  movies.forEach((film) => {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  });
});
