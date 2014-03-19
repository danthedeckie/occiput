function start_getting(sections) {
    var i,
        again = function(){start_getting(sections);};

    for (i=0; i<sections.length; i++) {
        $.get('/script/' + sections[i], function(s){ return function(data) {
            var type = $('#content_' + s).data('type'),
                new_html = '';

            switch (type) {
                case 'svg':
                    //new_html = '<svg width="200px" height="200px">' + data['data'] + '</svg>';
                    new_html = data['data'];
                    break;
                case 'html':
                    new_html = data['data'];
                    break;
                case 'pretext':
                default:
                    new_html = '<pre>' + data['data'] + '</pre>';
            }
            $('#content_' + s).html(new_html);

        }}(sections[i]));
    }
    setTimeout(again, 2000);

}
