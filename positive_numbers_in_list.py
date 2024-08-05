# removing negative numbers in the list
n=int(input('enter the no of elements'))
list1=[]
for i in range(n):
    print('enter the number')
    list1.append(int(input()))
for j in list1:
    if j < 0:
        list1.remove(j)
print('Output:',list1)
