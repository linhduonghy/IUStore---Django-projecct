$('#btnMinus').on('click', () => {
    let qty = +($('#qtyValue').val())
    if (qty == 1) {
        return
    }
    $('#qtyValue').val(qty - 1)
})

$('#btnAdd').on('click', () => {
    let qty = +($('#qtyValue').val())
    $('#qtyValue').val(qty + 1)
})