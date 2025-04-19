// Handling form submission
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
  event.preventDefault();
  alert("Message sent!");  // Simple alert when form is submitted
  form.reset();  // Reset form after submission
});
