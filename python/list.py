# pop

a = [1,2,4,78,94,4]
a.pop()
print(a)
a.pop(2)
print(a)


# index
a = [1,2,4,78,94,4]
print(a.index(2))

# remove

b = [1,2,4,78,94,4, 5]
b.remove(5)
print(b)

# extend
c = [4,5]
d = [6,7]

c.extend(d)
print(c)

# append
c.append('a')
c.append([90,100])

print(c)

# clear
y = [354, 45, 78]
print(y)
y.clear()
print(y)


# pointer
s = [3,6,7]
t = s   # they point to each other now
t.append(89)
print(s)

# sort ascending descending
i = [2,367, 4]
i.sort()
print(i)
j = [3,1,98]
j.sort(reverse=True)
print(j)

# copy -> shallow copy
k = [1,2,3]
l = k.copy()
l.append('boojie')
print(k)
print(l)

# copy -> deepcopy for nested lists
