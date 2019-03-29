var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('order_received', function(msg) {
    console.log(msg.data);
    $('#orders_table tbody').append(
        '<tr class="animate">' +
        '<td>' + '</td>' +
        '<td>' + msg.data.nombre_cliente + '</td>' +
        '<td>' + msg.data.direccion_cliente + '</td>' +
        '<td>' + msg.data.telefono_cliente + '</td>' +
        '<td>' + msg.data.orden + '</td>' +
        '</tr>'
    );
});