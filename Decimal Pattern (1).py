a=int(input("Enter the number of rows:"))
if (a<=0 ):
     print("Enter the valid number of rows to be printed")
else:
    for i in range(a+1):
        for j in range(1,i+1):
            print(j/10,end=" ")
        print("\n")
