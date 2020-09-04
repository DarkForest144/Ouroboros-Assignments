#Bubble sort

arr= input('Enetr list elements: ').split()
print(arr)
for i in range(len(arr)):
    # print('iteration ',i)
    flag=0 
    for j in range(len(arr)-1):

        if arr[j]>=arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            flag=1
            # print(arr)

    if flag == 0:
        print("Already sorted")
        break


print('Sorted list: ',arr)

