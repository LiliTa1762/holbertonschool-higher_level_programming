$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json'
})
// If the request is done continue with done
// The response is passed to the function
  .done(function (data) {
    $('DIV#character').html(data.name);
  });
