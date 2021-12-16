
nrow = int(input("Enter the number of rows:"))


for i in range(0,nrow-1):
    for y in range(0,i+1):
        print("*", end=" ")
    print()    