lst=["apple","grape","mango"]
print(lst)
print(type(lst))
print(lst[1])

#indexing
lst1=[10,11,12,13,14,15]
print(lst1[2])

#slicing
print(lst1[1:5])
print(lst1[-4])
print(lst1[5:2])
print(lst1[5:2:-1])
print(lst1[5:2:-2])

#replacing
lst2=["apple","mango","grape","kiwi"]
print(lst2)
lst2[1]="banana"
print(lst2)

lst2.append("mango")
print(lst2)

lst2.insert(2,"cherry")
print(lst2)

lst2.pop()
print(lst2)

lst2.pop(3)
print(lst2)

lst3=["apple","mango","grape","kiwi","Apple","Cherry","banana"]
lst3.sort()
print(lst3)

lst3.remove("kiwi")
print(lst3)
lst3.remove(3)
print(lst3)

lst3.clear()
print(lst3)

print("hjello")