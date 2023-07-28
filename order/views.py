from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Tables,Items,Categories,Orders,Delivered





def placeorder(request,table):
    current_table = Tables.objects.get(id=table)
    current_table.status=1 #occupied table
    current_table.save()
    update_order = Orders.objects.filter(table_id=table)#only make order when

    for i in update_order:
        item_selected=Items.objects.filter(id=i.item.id).first()
        #item_selected.item_remain = item_selected.item_remain - i.quantity
        item_selected.selected_itm = 0
        # currentitems = Items.objects.filter(id=i.item.id)
        item_selected.save()
        i.ordered=True
        i.delivered=False
        i.save()

    context={
        'table':table
    }
    return render(request,"message_orderplaced.html",context)

def checkoutitem(request,table):
    deli=Delivered.objects.filter(table_id=table).first()
    order=Orders.objects.filter(table_id=table).first()
    cartitem = Orders.objects.filter(table_id=table)
    total_price=0
    for i in cartitem:
        total_price = total_price + (i.item.item_price * i.quantity)
    context={
        'table':table,
        'cartitem': cartitem,
        'total_price':total_price
    }
    if deli :
        return render(request,"nextOrder/displayOrderedItem2.html",context)
    elif order:
        return render(request,"displayOrderedItem.html",context)
    else:
        return render(request,"displayOrderedItem.html",context)






def addquantitytoorder(request):


    if request.method=="POST":
        itm_id=int(request.POST.get('product_id'))
        itm_qty=int(request.POST.get('product_qty'))
        table =(request.POST.get('table'))
        item_check=Items.objects.get(id=itm_id)
        # order_check=Orders.objects.filter(item_id=itm_id)
        if (itm_qty > 0):
            if(item_check):
                if(Orders.objects.filter(table_id=table,item_id=itm_id)):
                    neworder = Orders.objects.get(item_id=itm_id,table_id=table)
                    if(itm_qty <= item_check.item_remain):
                        neworder.quantity=itm_qty
                        if(item_check.selected_itm < itm_qty):#incrementing itm_qty
                            item_check.item_remain=item_check.item_remain-1
                            if(item_check.item_remain==0):
                                item_check.status=True
                                item_check.save()
                        else:
                            item_check.item_remain=item_check.item_remain+1
                        item_check.selected_itm=itm_qty
                        item_check.save()
                        neworder.save()
                        return JsonResponse({'status':"quantity updated"})

                    else:
                        return JsonResponse({'status':"item outof stock"})
                else:
                    if(item_check.selected_itm < itm_qty):#incrementing itm_qty
                        item_check.item_remain=item_check.item_remain-1
                        if(item_check.item_remain==0):
                                item_check.status=True
                                item_check.save()
                    else:
                        item_check.item_remain=item_check.item_remain+1
                    item_check.selected_itm=itm_qty
                    item_check.save()
                    Orders.objects.create(table_id=table,item_id=itm_id,quantity=itm_qty)
                    return JsonResponse({'status':"item added successfuly"})
            else:
                return JsonResponse({'status':"This item does not exist"})
        else:#(itm_qty==0)
            orderdelete= Orders.objects.get(item_id=itm_id,table_id=table)
            orderdelete.delete()
            item_check.item_remain=item_check.item_remain+1
            item_check.selected_itm=itm_qty
            item_check.save()
            return JsonResponse({'status':"order item deleted"})
    else:
        return redirect('/')


def index(request):
    tab = Tables.objects.all()
    deli = Delivered.objects.filter(paid=False)
    context={
        'tab':tab,
        'deli':deli
    }
    return render(request,'index.html',context)

def nextorder(request,table):
    category=Categories.objects.filter(status=0)
    item = Items.objects.all()
    tb= Tables.objects.get(id=table)
    order = Orders.objects.filter(table=table)
    deli = Delivered.objects.filter(paid=False,table=table)#deli=delivered 's object
    total_price=0
    for d in deli:
        total_price = total_price + (d.item.item_price * d.quantity)


    if(order):
        for o in order:
            for i in item:
                if(o.item.id==i.id):
                    i.selected_itm=o.quantity
                    i.save()

    else:
        for i in item:
            i.selected_itm = 0
            i.save()


    context = {
        'tb':tb,
        'table':table,
        'category':category,
        'item':item,
        'deli':deli,
        'total_price':total_price
    }
    return render(request,'nextOrder/nextordertest.html',context)

def tableselect(request,table):
    category=Categories.objects.filter(status=0)
    item = Items.objects.all()
    order = Orders.objects.filter(table=table)
    tb = Tables.objects.get(id=table)

    if(order):
        for o in order:
            for i in item:
                if(o.item.id==i.id):
                    i.selected_itm=o.quantity
                    i.save()
    else:
        for i in item:
            i.selected_itm = 0
            i.save()
    context = {
        'tb':tb,
        'table':table,
        'category':category,
        'item':item,
        'order':order
    }
    return render(request,'list_items.html',context)

def categoryselected(request,category,table):
    order = Orders.objects.filter(table=table)
    categorylist=Categories.objects.filter(status=0)
    if(category==0):
        itemlist = Items.objects.filter(status=0)
    else:
        itemlist = Items.objects.filter(category__id=category,status=0)
    for o in order:
        for i in itemlist:
            if(o.item.id==i.id):
                i.selected_itm=o.quantity
    context={
        'item':itemlist,
        'table':table,
        'order':order,
        'category':categorylist,

    }
    return render(request,"list_items.html",context)

# def clearallselectedqty(request,table):
#     category=Categories.objects.filter(status=0)
#     order = Orders.objects.filter(table=table)
#     clearitem = Items.objects.filter(status=0)
#     for i in clearitem:
#         i.selected_itm=0
#         i.save()


#     for o in order:
#         for i in clearitem:
#             if(o.item.id==i.id):
#                 i.selected_itm=o.quantity
#     context={
#         'table':table,
#         'category':category,
#         'item':clearitem,
#         'order':order
#     }
#     return render(request,'list_items.html',context)


def tableSelect(request,table_name):
    print(table_name)
    item = Items.objects.all()
    context={
        'item':item
    }
    return render(request,'tableselected.html',context)




