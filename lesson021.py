
thislist = ['apple', 'banana', 'cherry']
print(thislist)
print(len(thislist))
thislist.clear()
print(thislist)
print(len(thislist))


thislist = ['apple', 'banana', 'cherry']
list3 = thislist.copy()
print(list3)
print(len(list3))
print(thislist is list3)
print(thislist == list3)
print()

list3.remove('apple')
print(list3)
print(len(list3))


