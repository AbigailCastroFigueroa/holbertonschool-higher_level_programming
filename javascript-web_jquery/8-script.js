$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const movies = data.results;
    for (let index = 0; index < movies.length; index++) {
      const listItem = movies[index].title;
      $('UL#list_movies').append('<li>' + listItem + '</li>');
    }
  });
});
