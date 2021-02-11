$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json'
})
  .done(function (data) {
    $('DIV#hello').html(data.hello);
  });
