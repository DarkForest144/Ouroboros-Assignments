#question - star pattern

n = int(input("Enter value of n- "))
star = 1
hash = n - star

for i in range(1,(n+1)):
    if i % 2 != 0:
        print ("* "  *  star,end='')
        print ("# "  *  hash,end='')

    else :
        print ("# " * hash,end='')
        print ("* " * star,end='')

    if(i< n ):
        star += 1
        hash -= 1
    else:
        star -= 1
        hash += 1
    print()