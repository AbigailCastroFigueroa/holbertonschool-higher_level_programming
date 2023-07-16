$(document).ready(function () {
  $('#add_item').click(function () {
    const listElement = $('<li>Item</li>');
    $('ul.my_list').append(listElement);
  });
});
