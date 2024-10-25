   
       $(function () {       
        $('#greetings').DataTable({
          "paging": true,
          "searching": true,
          "ordering": false,
        });
      });
   
    
        // Wait for DOM content to be loaded
        document.addEventListener('DOMContentLoaded', function () {
          const dropdown = document.querySelector('.nav-item.dropdown');
      
          // Toggle dropdown on click for mobile screens
          dropdown.addEventListener('click', function (event) {
            event.stopPropagation(); // Prevents click event from closing immediately
            dropdown.classList.toggle('show'); // Toggle visibility
            dropdown.querySelector('.dropdown-menu').classList.toggle('show');
          });
      
          // Close dropdown if clicking outside of it
          document.addEventListener('click', function (event) {
            if (!dropdown.contains(event.target)) {
              dropdown.classList.remove('show');
              dropdown.querySelector('.dropdown-menu').classList.remove('show');
            }
          });
        });
