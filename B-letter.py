for row in range(11):
    for col in range(6):
        if ((row==1 or row==10 or col==1) or (row-col==4) or (row-col==1) or (row-col==3)):
            print("*",end="")
        else:
            print(end=" ")
    print()      