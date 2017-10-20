$(function(){
    $('#search').keyup(function(){
        $.ajax({
            type: "GET",
            url: "/home/search-suggest",
            data:{
                'queryset_list': $('#search').val(),
            },
            success: search.Success,
            dataType: 'html'
        });
    });
});
function searchSuccess(data, textSatus, jqXHR){
    $('#search-suggest').html(data);
}