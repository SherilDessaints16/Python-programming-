Sheril=[]
a= int(input("Enter the number of elements you want to print : "))
b= str(input("Order (A/D): "))
for i in range(a):
    c= str(input(" "))
    Sheril.append(c)
Sheril.sort()
if (b == 'A'):
    for she in Sheril:
        print(she)
else:
    Sheril.sort(reverse=True)
    for she in Sheril:
        print(she)
    
