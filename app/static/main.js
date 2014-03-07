function start_getting(sections) {
    var i;

    for (i=0; i<sections.length; i++) {
        $.get('/script/' + sections[i], function(s){ return function(data) {
            var type = $('#content_' + s).data('type');
            switch (type) {
                case 'pretext':
                default:
                    $('#content_' + s).html('<pre>' + data['data'] + '</pre>');
            }
        }}(sections[i]));
    }

}
