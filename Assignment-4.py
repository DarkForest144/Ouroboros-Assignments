#Selection sort

def selSort(Lst):
    for i in range(0, len(Lst) - 1):
        sm = i
        for j in range(i + 1, len(Lst)):
            if Lst[j] < Lst[sm]:
                sm = j
        Lst[i], Lst[sm] = Lst[sm], Lst[i]
 
 
Lst = input('Enter the list of numbers: ').split()
Lst = [int(x) for x in Lst]
selSort(Lst)
print('Sorted list: ', Lst)