// Wait until the entire HTML document is fully loaded and parsed
document.addEventListener('DOMContentLoaded', () => {
  // Select the button element with the ID 'start-btn'
  const btn = document.getElementById('start-btn');
  
  // Check if the button exists on the page to avoid errors
  if (btn) {
    // Add a click event listener to the button
    // When the button is clicked, it will call the `toForm` function
    btn.addEventListener('click', toForm);
  }
});

// Define the function that will be triggered when the button is clicked
function toForm() {
  // Get the button element again (optional, since it's already selected earlier)
  const btn = document.getElementById('start-btn');
  
  // Retrieve the value of the custom attribute 'data-url' from the button
  const url = btn.getAttribute('data-url');
  
  // Redirect the browser to the URL stored in the 'data-url' attribute
  window.location.href = url;
}
