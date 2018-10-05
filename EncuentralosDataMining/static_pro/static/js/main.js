$('form.ajax').on('submit',function(){
    var that = $(this),
        url = that.attr('action'),
        method = that.attr('method'),
        data = {},

     that.find('[name]').each(function(index, value){
        console.log(value);
     });
    return false;
})