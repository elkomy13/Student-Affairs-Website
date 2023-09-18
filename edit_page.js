function updateStudent() {
  var form = $('.update');
  var url = form.attr('action');
  var data = form.serialize();

  $.ajax({
    type: 'POST',
    url: url,
    data: data,


success: function(response) {
    // Display a success message
    alert("Student updated successfully");
    location.reload();
  },
  error: function(response) {
    // Display an error message
    alert("An error occurred. Please try again.");

    location.reload();
  }
  });

}




