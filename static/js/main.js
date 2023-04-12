let link_a = document.querySelectorAll('.link a')
let close = true
console.log(link_a)

link_a.forEach(function (t, i) {
    t.addEventListener('click', function (e) {
        e.preventDefault()
        close = true
        for (const n of link_a) { n.classList.remove('active') }
        //console.log('----')
        if (close == true) {
            link_a[i].classList.add('active')
            close = false
        } else {
            close = true
        }

    })
})