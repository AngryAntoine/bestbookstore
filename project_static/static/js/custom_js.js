function initDateFields() {
    $('input#id_publish_date').datepicker({
        format: 'yyyy-mm-dd'
    });
}

$(document).ready(function(){
    initDateFields();
});
