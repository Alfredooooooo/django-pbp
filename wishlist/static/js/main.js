$(document).ready(function() {
    findData()
})

$('inginSubmit').on('submit', (e) => {
    e.preventDefault();
    let form = $(this);
    let urls = form.attr('action')
    $.ajax({
        url: urls,
        type: 'POST',
        data: form.serialize(),
        success: (data) => {
            let dt = data.data;
            $(tbody).innerHTML += `<tr>${dt.nama_barang}</tr><tr>${dt.harga_barang}</tr><tr>${dt.deskripsi}</tr>`
        }
    })
})


function findData() {
    $.get('/wishlist/json', function(data) {
        dataJSON = JSON.parse(data);
        $.each(dataJSON, function(dt) {
            $(tbody).innerHTML += `<tr>${dt.nama_barang}</tr><tr>${dt.harga_barang}</tr><tr>${dt.deskripsi}</tr>`
        })
    })
}

