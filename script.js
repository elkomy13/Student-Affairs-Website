function makeAjaxRequest() {// Get the form data
  const email = document.getElementById("email").value;
  const password = document.getElementById("fpass").value;

  // Make AJAX request
  fetch('/ajax/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email, password })
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response data
      console.log(data);
    })
    .catch(error => {
      // Handle any errors
      console.error('Error:', error);
    });
}

function validEmail(mail) {
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(mail).toLowerCase());
}
function validatePassword(password) {
  const re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*[@$!%*?&]).{8,}$/;
  return re.test(password);
}

// Add event listener to the form submission
document.querySelector("form").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent the default form submission

  const email = document.getElementById("email").value;
  const password = document.getElementById("fpass").value;
  const verifyPassword = document.getElementById("spass").value;

  // Validate email
  if (!validEmail(email)) {
    document.getElementById("email-error").textContent = "Invalid email address";
    return;
  }

  // Validate password
  if (!validatePassword(password)) {
    document.getElementById("password-error").textContent = "At least 8\none lowercase letter\none uppercase letter\none digit\none letter (either lowercase or uppercase)"
    ;
    return;
  }

  // Check if passwords match
  if (password !== verifyPassword) {
    document.getElementById("password-error").textContent = "Passwords do not match";
    return;
  }

  // All validations passed, make AJAX request
  makeAjaxRequest();
});
