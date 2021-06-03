$('.qty-add').on('click', () => {
    console.log(123);
    let qty_value = $(this).closest('.qty-input').find('.qty-value');
    
    $(this).closest('')
})

$('.qty-minus').on('click', () => {
    let qty_value = $(this).closest('.qty-input').find('.qty-value');
    if (+(qty_value) == 1) {
        return
    }
})