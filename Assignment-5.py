#Bubble sort

Lst= input('Enetr list elements: ').split()
print(Lst)
for i in range(len(Lst)):
    # print('iteration ',i)
    flag=0 
    for j in range(len(Lst)-1):

        if Lst[j]>=Lst[j+1]:
            Lst[j],Lst[j+1]=Lst[j+1],Lst[j]
            flag=1
            # print(Lst)

    if flag == 0:
        break


print('Sorted list: ',Lst)

