$(document).ready(function(){
  console.log("test2");

  const dropdown = document.querySelector('.selected');
  const menu = document.querySelector('.options')
  const selectSubmit = document.querySelector('.submit-button');

  dropdown.addEventListener('click', () => {
    menu.classList.toggle("active");
  });

  options = document.querySelectorAll(".option");

  options.forEach(o => {
      o.addEventListener("click", () => {
        dropdown.innerHTML = o.querySelector('label').innerHTML;
        menu.classList.remove("active");
      });
    });


  var csrftoken = getCookie('csrftoken');

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });


  $('.search').submit(function(event) {
    event.preventDefault();

    $('data-row').html("");
    var studentId = $('#search').val().trim();

    $.ajax({
      url: "/assign/student/",
      type: "POST",
      data: {
        student_id: studentId
      },
      dataType: 'json',
      success: function(data){
        const dataTable = $('#data-row');
        parsedData = JSON.parse(data);
        student = parsedData[0];
        console.log(student);
        dropdown.innerHTML = "Choose department";
        if (student !== undefined) {
          dataTable.children().eq(0).html(student.pk);
          dataTable.children().eq(1).html(student.fields.name);
          dataTable.children().eq(2).html(student.fields.GPA);
          dataTable.children().eq(3).html(student.fields.level);
          dataTable.children().eq(4).html(student.fields.phone);
          dataTable.children().eq(5).html(student.fields.department);
          if (student.fields.level < 3) {
            dropdown.disabled = true;
            menu.disabled = true;
            selectSubmit.disabled = true;
          }
          else{
            dropdown.disabled = false;
            menu.disabled = false;
            selectSubmit.disabled = false;
          }
        }
        else {
          dataTable.children().eq(0).html("");
          dataTable.children().eq(1).html("");
          dataTable.children().eq(2).html("");
          dataTable.children().eq(3).html("");
          dataTable.children().eq(4).html("");
          dataTable.children().eq(5).html("");
          dropdown.disabled = true;
          menu.disabled = true;
          selectSubmit.disabled = true;
        }

      }
    })
  })



  $('.choose').submit(function(event){
    event.preventDefault();
    var selectedId = $('#data-row').children().eq(0).html().trim();
    var selectedDepartment = $('.selected').html().trim();

    $.ajax({
      url: '/assign/update/',
      type: 'POST',
      data: {
        student_id: selectedId,
        department: selectedDepartment
      },
      dataType: 'json',
      success: function(data){
        const dataTable = $('#data-row');
        parsedData = JSON.parse(data);
        student = parsedData[0];
        dataTable.children().eq(0).html(student.pk);
        dataTable.children().eq(1).html(student.fields.name);
        dataTable.children().eq(2).html(student.fields.GPA);
        dataTable.children().eq(3).html(student.fields.level);
        dataTable.children().eq(4).html(student.fields.phone);
        dataTable.children().eq(5).html(student.fields.department);
      }
    })
  })


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