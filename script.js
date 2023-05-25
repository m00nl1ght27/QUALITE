const toggleSwitch = document.getElementById('toggle-switch');
const body = document.body;

function flipImage() {
  var image = document.getElementById("shiv-image");
  image.classList.toggle("flipped");
}

function toggleTheme() {
  var body = document.body;
  body.classList.toggle("dark-theme");
  body.classList.toggle("light-theme");
}

toggleSwitch.addEventListener('change', () => {
  if (toggleSwitch.checked) {
    body.classList.add('dark-theme');
  } else {
    body.classList.remove('dark-theme');
  }
});

