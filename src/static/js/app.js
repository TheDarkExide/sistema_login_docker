let showingLogin = true;
const slider = document.getElementById('slider');
const toggleText = document.getElementById('toggleText');
const toggleLink = document.getElementById('toggleLink');

toggleLink.addEventListener('click', () => {
  if (showingLogin) {
    slider.style.transform = 'translateX(-50%)';
    toggleText.firstChild.textContent = '¿Ya tienes cuenta? ';
    toggleLink.textContent = 'Inicia sesión';
  } else {
    slider.style.transform = 'translateX(0%)';
    toggleText.firstChild.textContent = '¿No tienes cuenta? ';
    toggleLink.textContent = 'Regístrate';
  }
  showingLogin = !showingLogin;
});
