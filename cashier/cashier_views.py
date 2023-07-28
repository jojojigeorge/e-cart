from django.shortcuts import render
from django.http import HttpResponse
from order.models import Tables,Items,Categories,Orders,Delivered


# Create your views here.


def billpaid(request,table):
  selectedtable = Tables.objects.get(id=table)
  selectedtable.status = False
  selectedtable.save()
  return render(request,'cashier/redirecttomain.html')

 
 
def cashierindex(request):
  table=Tables.objects.filter(status=True)
  context={
    'table':table
  }
  return render(request,'cashier/cashierindex.html',context)



def billredy(request,table):
  deli = Delivered.objects.filter(table_id=table,paid=False)
  grandtotal=0
  for d in deli:
    grandtotal = grandtotal + (d.quantity *d.item.item_price)
  context={
    'deli':deli,
    'grandtotal':grandtotal,
    'table':table
  }
  return render(request,'cashier/billredy.html',context)



def billtableselect(request,table):
  deli=Delivered.objects.filter(table_id=table)
  order = Orders.objects.filter(table_id=table,delivered=False)
  tablelist=Tables.objects.filter(id=table)
  print(tablelist)
  grandtotal=0
  for d in deli:
    grandtotal = grandtotal + (d.quantity *d.item.item_price)


  context={
    'tb':table,
    'table':tablelist,
    'order':order,
    'deli':deli,
    'grandtotal':grandtotal
  }
  return render(request,'cashier/billtableselect.html',context)