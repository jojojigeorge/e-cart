$(document).ready(function () {
    
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        var inc_value=$(this).closest('.product_data').find('.qty_input').val();
        var value = parseInt(inc_value,10);
        value=isNaN(value) ? 0 : value;
        if( value < 10 )
        {
            value++;
            $(this).closest('.product_data').find('.qty_input').val(value);

        }
    });



    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        var dec_value=$(this).closest('.product_data').find('.qty_input').val();
        var value = parseInt(dec_value,10);
        
        value=isNaN(value) ? 0 : value;
        if( value > 0 )
        {
            value--;
            $(this).closest('.product_data').find('.qty_input').val(value);

        }
    });
   


    
    $('.changeQuantity' ).click(function (e) { 
        e.preventDefault();
        var product_id=$(this).closest('.product_data').find('.prod_id').val();
        var product_qty=$(this).closest('.product_data').find('.qty_input').val();
        var table=$(this).closest('.product_data').find('.tab_id').val();
        

        // var dec_value=$(this).closest('.tabledata').find('.tab_id').val();
        // var table = parseInt(dec_value,10);


        var token=$('input[name=csrfmiddlewaretoken').val();
        // print("in custom.js")
        // print(table_id,product_id,product_qty)
        $.ajax({
            method:"POST",
            url: "/addquantitytoorder",
            data: {
                'product_id':product_id,
                'product_qty':product_qty,
                'table':table,
                csrfmiddlewaretoken:token
            },
           
            success: function (response) {
                alertify.success(response.status)
            }
        });
        // print(product_id,product_qty,table_id)

        
    });





















   
});