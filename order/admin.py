from django.contrib import admin
from .models import Tables,Categories,Items,Orders,Delivered


# Register your models here.

admin.site.register(Categories)
admin.site.register(Tables)
admin.site.register(Items)
admin.site.register(Orders)
admin.site.register(Delivered)
# from .models import Tables,Items,Categories,Orders
                                         
# Register your models here.
# class OrdersAdmin(admin.ModelAdmin):
#     list_display= ['table.table_name']
# admin.site.register(Orders,OrdersAdmin)

# #register GetOrder table
# class GetOrderAdim(admin.ModelAdmin):
#     list_display= ['get_item','get_quantity']
# admin.site.register(GetOrder,GetOrderAdim)

# class ItemAdmin(admin.ModelAdmin):
     
#      list_display = ['i_name', 'i_total', 'i_remain','i_price', ] 
    
# admin.site.register(Item,ItemAdmin)

# class OrdertableAdmin(admin.ModelAdmin):
#    list_display = ['t_name','i_name','item_quantity']
# admin.site.register(Order_table,OrdertableAdmin)
