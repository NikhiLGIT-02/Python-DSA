item=input("Enter Item: ")
qty = int(input('Enter Quantity: '))
Price = float(input('Enter Price per Unit: '))
Sub_total = qty*Price
n=int(input('Is a member (1 for YES || 0 for NO ): Soa'))

if n==1:
        dis = Sub_total * 0.10
total=Sub_total-dis
    
 
if total>500:
    gst=total*0.05
else:
    gst=total*0.12
fa=total+gst
print('Item: ',item)
print('Quantity: ',qty)
print('Price: ',Price)
print('Subtotal: ',Sub_total)
print('Discount: ',dis)
print('Total: ',total)
print('GST: ',gst)
print('Final Amount: ',fa)