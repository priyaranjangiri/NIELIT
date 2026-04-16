s={1,2,3,4,5}
print(s)

s.add(6)
print(5)

s.remove(3)
print(s)

s.update({7,8})
print(s)

s.discard(2)
print(s)

s.pop()
print(s)

s.clear()
print(s)

a={1,2,3}
b={3,4,5}
print(a.union(b))  
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))

m={1,2,3,4,5}
n={3,4,5}
p={7,8,9}
print(n.issubset(m))
print(m.issuperset(n))
print(m.isdisjoint(p))


