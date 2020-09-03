# Question-  https://www.hackerrank.com/challenges/arrays-ds/problem

def Rev(lst): 
    return [ele for ele in reversed(lst)] 



n = int(input('Enter size of array: '))
lst = []

print('Enter Elements of the list: ')
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 
print(Rev(lst)) 


