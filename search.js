$(document).ready(function(){
  console.log("test1");
  var csrftoken = getCookie('csrftoken');

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });


  $('form.search').submit(function(event) {
    event.preventDefault();
    console.log('Form submitted');
    var studentName = $('#search').val().trim();
    $('#data').html("");
    $.ajax({
      url: '/search/result/',
      type: 'POST',
      data: {
        student_name: studentName
      },
      dataType: 'json',
      success: function(data) {
        if (data.students.length != 0) {
          var dataArray = JSON.parse(data.students);
          console.log(dataArray[0]);
          dataArray.forEach(function(student) {
            const row = $('<tr>');
            $('<td>').text(student.pk).appendTo(row);
            $('<td>').text(student.fields.name).appendTo(row);
            $('<td>').text(student.fields.GPA).appendTo(row);
            $('<td>').text(student.fields.gender).appendTo(row);
            $('<td>').text(student.fields.level).appendTo(row);
            $('<td>').text(student.fields.department).appendTo(row);
            $('<td>').text(student.fields.email).appendTo(row);
            $('<td>').text(student.fields.phone).appendTo(row);

            $('#data').append(row);
          });
        }
      }
    })
  });

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

})