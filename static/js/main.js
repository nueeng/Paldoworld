const link_a = document.querySelectorAll('.link a');
const home_a = document.querySelector('.home_a')
// let close = true;

home_a.addEventListener('click', function () {
    link_a[0].classList.add('active1');
    for (let i = 1; i <= 4; i++) {
        link_a[i].classList.remove('active1');
    }
    localStorage.setItem('activeLink', link_a[0].href);
});

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
            localStorage.removeItem('activeLink');
        }
    });
}
