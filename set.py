x={1,4,3,10,20,"car","bit"}
print(x)
print(type(x))

x.add("arun")
print(x)

x.pop()
print(x)


x.remove("bit")
print(x)

x.discard("arun")
print(x)




l4=[2,10,9,"nea","sree"]
print(l4)

l5=["mango","apple","orange"]
l4.extend(l5)
print(l4)


t1=(2,4,7,27,84)
print(t1)
t2=list(t1)
print(t2)

t2.insert(5,"green")
print(t2)

t2.index(84)
print(t2)

print(t2[1:4])
print(t2[2])

# update


s1={"a","b","c","d"}
s2={"e","f","g"}
s1.update(s2)
print(s1)

# union


s1={"a","b","c","d"}
s2={"e","f","c","d"}
z=s1.union(s2)
print(z)

s1={"a","b","c","d"}
s2={"e","f","c","d"}
y=s1.difference(s2)
print(y)

s1={"a","b","c","d"}
s2={"e","f","c","d"}
z=s1.intersection(s2)
print(z)