#Insertion sort

Lst= input('Enter elements in list: ').split()
for i in range(1,len(Lst)):
    key = Lst[i]
    j=i-1
    while j>=0 and key<Lst[j]:
        Lst[j+1]=Lst[j]
        j-=1

    Lst[j+1]=key

print(Lst)