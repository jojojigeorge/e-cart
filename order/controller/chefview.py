from django.http import JsonResponse
from django.shortcuts import redirect, render
from order.models import Orders,Tables,Delivered


def tablewiseorder(request):
    table = Tables.objects.all()
    order = Orders.objects.filter(delivered=False)
    context = {
        'table':table,
        'order':order
    }
    return render(request,'chefTemplate/tablewiseorder.html',context)


def listorders(request):
    orderlist=Orders.objects.filter(delivered=False)
    context={
        'order':orderlist
    }
    return render(request,'chefTemplate/listorders.html',context)

# delivered button clicked in table wise order list 
def item_delivered(request,order):
    currentorder = Orders.objects.get(id=order)
    currentorder.delivered=True
    currentorder.ordered=False
    currentorder.save()

     # transfer data from Orders to Delivered table
    deli = Delivered.objects.filter(table_id=currentorder.table_id,item_id=currentorder.item_id).first()
    if(deli):
        deli.quantity=deli.quantity+currentorder.quantity
        deli.save()
    else:
        # transfer data from Orders to Delivered table
        Delivered.objects.create(
            customer_name=currentorder.customer_name,
            table = currentorder.table,
            item = currentorder.item,
            quantity = currentorder.quantity,
            order_note=currentorder.order_note,
            
        )

    ordernow = Orders.objects.get(id = order)
    ordernow.delete()
    table = Tables.objects.all()
    order = Orders.objects.filter(delivered=False)
    context = {
        'table':table,
        'order':order
    }
    return render(request,'chefTemplate/tablewiseorder.html',context)
# all order summary not ordered by table wise  
def itemdelivery(request,order):
    currentorder = Orders.objects.get(id=order)
    currentorder.delivered=True
    currentorder.ordered=False
    currentorder.save()
    
    deli = Delivered.objects.filter(table_id=currentorder.table_id,item_id=currentorder.item_id).first()
    if(deli):
        deli.quantity=deli.quantity+currentorder.quantity
        deli.save()
    else:
        # transfer data from Orders to Delivered table
        Delivered.objects.create(
            customer_name=currentorder.customer_name,
            table = currentorder.table,
            item = currentorder.item,
            quantity = currentorder.quantity,
            order_note=currentorder.order_note,
            
        )

    ordernow = Orders.objects.get(id = order)
    ordernow.delete()
    orderlist=Orders.objects.filter(delivered=False)
    context={
        'order':orderlist
    }
    return render(request,'chefTemplate/listorders.html',context)
