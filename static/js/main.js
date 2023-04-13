    const link_a = document.querySelectorAll('.link a');
    let close = true;

    // Check if there is a value stored in localStorage for the button
    if (localStorage.getItem('activeButton')) {
        // Get the index of the active button from localStorage
        const activeButtonIndex = parseInt(localStorage.getItem('activeButton'));

        // Add the active class to the button
        link_a[activeButtonIndex].classList.add('active1');
        close = false;
    }

    link_a.forEach(function (t, i) {
        t.addEventListener('click', function (e) {
            // e.preventDefault();
            close = true;

            // Remove the active class from all buttons
            for (const n of link_a) { n.classList.remove('active1'); }

            if (close == true) {
                // Add the active class to the clicked button
                link_a[i].classList.add('active1');
                close = false;

                // Save the index of the clicked button to localStorage
                localStorage.setItem('activeButton', i);
            } else {
                close = true;
            }
        });
    });