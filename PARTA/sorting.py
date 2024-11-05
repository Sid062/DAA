array=[]
n=int(input("Enter the number of elements "))
for i in range(0,n):
    ele=int(input("Enter the element"))
    array.append(ele)
print("Elements before sorting ",array)
for i in range(n):
    minimum=i
    for j in range(i+1,n):
        if array[j]<array[minimum]:
            minimum=j
    temp=array[i]
    array[i]=array[minimum]
    array[minimum]=temp
print("Elements after sorting ",array)