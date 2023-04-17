const link_a = document.querySelectorAll('.link a');
let close = true;

if (localStorage.getItem('activeButton')) {
    const activeButtonIndex = parseInt(localStorage.getItem('activeButton'));

    link_a[activeButtonIndex].classList.add('active1');
    close = false;
}
for (const n of link_a) {
    n.classList.remove('active1');
}
link_a.forEach(function (t, i) {
    t.addEventListener('click', function (e) {
        close = true;

        for (const n of link_a) {
            n.classList.remove('active1');
        }

        if (close == true) {
            link_a[i].classList.add('active1');
            close = false;
            localStorage.setItem('activeLink', t.href);
        } else {
            close = true;
        }
    });
});

if (localStorage.getItem('activeLink')) {
    const activeLink = localStorage.getItem('activeLink');

    link_a.forEach((link) => {
        if (link.href === activeLink) {
            link.classList.add('active1');
        }
    });
}
