
navButtons = document.querySelectorAll('.nav-item .nav-link');

const navButtonsArray = Array.from(navButtons);

navButtonsArray.forEach(element => {
  element.classList.remove('active');
  href = element.getAttribute('href');
  data =  element.getAttribute('data-active');
  if(href == data) {
   element.classList.add('active');
  }
});

