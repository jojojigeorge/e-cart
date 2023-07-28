from django.urls import path
from  order.controller import chefview
from . import views
from cashier import cashier_views
#now import the views.py file into this code




urlpatterns=[
# First page
path('',views.index,name='index'),
path('tableSelect/<table>',views.tableselect,name='tableselect'),
path('nextorder/<table>',views.nextorder,name='nextorder'),

path('listOrders',chefview.listorders,name='listorders'),
path('tablewiseorder',chefview.tablewiseorder,name='tablewiseorder'),
path('itemdelivery/<order>',chefview.itemdelivery,name='itemdelivery'),
path('item_delivered/<order>',chefview.item_delivered,name='item_delivered'),

path('cashier',cashier_views.cashierindex,name='cashier'),
path('billtableselect/<table>',cashier_views.billtableselect,name='billtableselect'),
path('billredy/<table>',cashier_views.billredy,name='billredy'),
path('billpaid/<table>',cashier_views.billpaid,name='billpaid'),



# Second page
path('addquantitytoorder',views.addquantitytoorder,name='addquantitytoorder'),
path('checkoutitem/<table>',views.checkoutitem,name='checkoutitem'),
# path('checkoutitem2/<table>',views.checkoutitem2,name='checkoutitem2'),
path('categoryselected/<category>/<table>',views.categoryselected,name='categoryselected'),
# path('clearallselectedqty/<table>',views.clearallselectedqty,name='clearallselectedqty'),

# Third page
path('placeOrder/<table>',views.placeorder,name='placeOrder'),



#path('displayOrderedItem',views.displayorder,name='displayorder'),
#path('tableSelect/<table_name>',views.tableSelect,name="tableselect")
#path('list_items',views.list_items,name='list_items')
# path('takeOrder/', views.takeOrder,name='takeOrder'),
#path('fetchdata/<t_name>', views.fetchdata,name='fetchdata'),
]

