var idPattern = /^\d{8}$/;
  var emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  var phonePattern = /^\d{11}$/;

  // Validate form on submission
  document.querySelector(".form").addEventListener("submit", function(event) {
    var idInput = document.getElementById("id");
    var emailInput = document.getElementById("mail");
    var phoneInput = document.getElementById("tele");

    // Validate ID
    if (!idPattern.test(idInput.value)) {
      alert("Invalid ID. It should be 8 numbers.");
      event.preventDefault(); // Prevent form submission
      return;
    }

    // Validate Email
    if (!emailPattern.test(emailInput.value)) {
      alert("Invalid email address.");
      event.preventDefault(); // Prevent form submission
      return;
    }

    // Validate Phone Number
    if (!phonePattern.test(phoneInput.value)) {
      alert("Invalid phone number. It should be 11 numbers.");
      event.preventDefault(); // Prevent form submission
      return;
    }

    // Form is valid, continue with submission
  });

window.addEventListener('DOMContentLoaded', () => {
  const levelInput = document.getElementById('lvl');
  const departmentInput = document.getElementById('DB');

  levelInput.addEventListener('change', () => {
    const selectedLevel = parseInt(levelInput.value);
    if (selectedLevel <= 2) {
      departmentInput.disabled = true;
    } else {
      departmentInput.disabled = false;
    }
  });
});
