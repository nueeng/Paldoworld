const link_a = document.querySelectorAll('.link a');
let close = true;

if (localStorage.getItem('activeButton')) {
    const activeButtonIndex = parseInt(localStorage.getItem('activeButton'));

    link_a[activeButtonIndex].classList.add('active1');
    close = true;
}


link_a.forEach(function (t, i) {
    t.addEventListener('click', function (e) {
        // e.preventDefault();
        close = true;

        for (const n of link_a) {
            n.classList.remove('active1');
        }
        if (close == true) {
            link_a[i].classList.add('active1');
            close = false;

            localStorage.setItem('activeButton', i);
        } else {
            close = true;
        }
    });
});
