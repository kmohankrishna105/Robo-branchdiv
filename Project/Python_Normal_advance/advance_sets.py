s=set()
s.add(1)
s.add(2)
print(s)

s.add(2)
print(s)

#s.clear()
print(s)

d={1,2,3,4,5,6}

# difference in sets mentioned above
print(d.difference(s))
print((d-s))


#d.discard('3')

#print(s.difference_update(d))

print(s.intersection(d))

#differencec_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)
#removes the matched values
print(x)

#intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
#removes the unmatched values
print(x)
