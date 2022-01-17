var $target = document.querySelector('.target')
var $button = document.querySelector('.mail-btn')
$button.addEventListener('click', function() {
    $target.classList.toggle('is-hidden')
})
