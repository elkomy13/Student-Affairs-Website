function updateStatus(checkbox, studentId) {
    const status = checkbox.checked ? 'Active' : 'Inactive';
    const url = '/update_status/';

    const csrftoken = getCookie('csrftoken'); // Get the CSRF token from the cookie

    fetch(url, { // Send the request using the Fetch API
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken, // Include the CSRF token
      },
      body: JSON.stringify({
        'student_id': studentId,
        'status': status,
      }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          console.log('Status updated successfully');
        } else {
          console.error('Failed to update status:', data.message);
        }
      })
      .catch(error => {
        console.error('An error occurred:', error);
      });
  }

  // Helper function to get the CSRF token from the cookie
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + '=') {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }