function validatePassword(password)
 {
    const re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;
    return re.test(password);
}
  const btn = document.querySelector('.Submitbtn');
  function myfunc(event) {
    const NEWPASS = document.getElementById('newpass').value;
    const ConfirmPass = document.getElementById('confirmpass').value;
    event.preventDefault();
    
    if (NEWPASS === ConfirmPass && validatePassword(NEWPASS))
     {
      localStorage.removeItem('Fpass');
      localStorage.removeItem('Spass');
      localStorage.setItem('Fpass', NEWPASS);
      localStorage.setItem('Spass', ConfirmPass);
      window.location.href = 'sign_in.html';
      alert('Password updated successfully!');
    } 
    else
    {
      alert('Please enter a valid password and make sure the two passwords match.');
    }
  }
  
  btn.addEventListener('click', myfunc);
  